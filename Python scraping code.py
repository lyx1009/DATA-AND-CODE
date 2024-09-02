import subprocess
import sys

# Function to install a package using pip
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install necessary packages
install('selenium')
install('webdriver_manager')
install('beautifulsoup4')
install('pandas')
install('openpyxl')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import pandas as pd
import re
import time

# Set the path to ChromeDriver and start Chrome browser
chrome_driver_path = 'C:/Program Files/Google/Chrome/Application/chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Define a function to calculate the starting index for each page
def get_page_index(page):
    return (page - 1) * 24  # Each page contains 24 properties

# Set total number of pages and the base URL
total_pages = 42  # 42 pages of data
base_url = 'https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E93959&sortType=6&propertyTypes=flat&includeSSTC=false&mustHave=&dontShow=&furnishTypes=&keywords=&index='
# sortType=6 is sort by "Newest listed"
# REGION: "%5E93959" is Hillingdon & propertyTypes: flat
# We will change each "REGION" index of 32 boroughs,
# and "propertyTypes" with flat, detached and terrace, one by one

data = []
# A list to store all property data

# Loop through each page to collect property data
for page in range(1, total_pages + 1):
    index = get_page_index(page)  # Calculate the index for the current page
    url = base_url + str(index)  # Construct the URL for the current page
    driver.get(url)  # Navigate to the page

    # Wait for the page to load completely
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'propertyCard')))
    except TimeoutException:
        print(f"Timeout occurred for page {page}")  # Print a message if loading times out
        continue  # Skip to the next page

    # Use Selenium to extract property ID, price, and link
    properties = driver.find_elements(By.CLASS_NAME, 'propertyCard')
    for property in properties:
        try:
            # Extract property ID
            anchor_tag = property.find_element(By.CLASS_NAME, 'propertyCard-anchor')
            property_id_full = anchor_tag.get_attribute('id')
            property_id = re.findall(r'\d+', property_id_full)[0] if property_id_full else 'N/A'

            # Extract price
            price = property.find_element(By.CLASS_NAME, 'propertyCard-priceValue').text.strip()

            # Extract property detail link
            href_tag = property.find_element(By.CLASS_NAME, 'propertyCard-link')
            href = href_tag.get_attribute('href')
            property_link = href if href else 'N/A'

            # Visit the property link to extract house type, bed, bath, size, and nearest station information
            if property_link != 'N/A':
                driver.get(property_link)
                time.sleep(3)  # Wait for the new page to load

                try:
                    house_type_tag = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, '_1hV1kqpVceE9m-QrX_hWDN'))
                    )
                    house_type = house_type_tag.text.strip() if house_type_tag else 'N/A'
                except TimeoutException:
                    house_type = 'N/A'

                try:
                    bedrooms = driver.find_element(By.XPATH, "//span[text()='BEDROOMS']/following::p").text.strip()
                except NoSuchElementException:
                    bedrooms = 'N/A'

                try:
                    bathrooms = driver.find_element(By.XPATH, "//span[text()='BATHROOMS']/following::p").text.strip()
                except NoSuchElementException:
                    bathrooms = 'N/A'

                try:
                    size = driver.find_element(By.XPATH, "//span[text()='SIZE']/following::p").text.strip()
                except NoSuchElementException:
                    size = 'N/A'

                try:
                    nearest_stations_container = driver.find_element(By.CLASS_NAME, '_2f-e_tRT-PqO8w8MBRckcn')
                    nearest_stations_info = nearest_stations_container.text.strip()
                except NoSuchElementException:
                    nearest_stations_info = 'N/A'

                driver.back()  # Go back to the main listings page
                time.sleep(2)  # Wait for the page to reload
            else:
                house_type = 'N/A'
                bedrooms = 'N/A'
                bathrooms = 'N/A'
                size = 'N/A'
                nearest_stations_info = 'N/A'
            # If no property link, set all details to 'N/A'
            # Append the extracted data to the data list
            data.append(
                {'ID': property_id, 'Price': price, 'HouseType': house_type, 'Beds': bedrooms, 'Baths': bathrooms,
                 'Size': size, 'NearestStations': nearest_stations_info, 'Link': property_link})
        except (NoSuchElementException, IndexError, StaleElementReferenceException):
            continue
           # Skip this property if any exception occurs

    # Convert to DataFrame and save to Excel
    df = pd.DataFrame(data)
    df.to_excel('D:\\7月21数据\\Flat\\Hillingdon-flat.xlsx', index=False)
    # We will save the data as each borough with each type, one by one

    # Close the driver
    driver.quit()


