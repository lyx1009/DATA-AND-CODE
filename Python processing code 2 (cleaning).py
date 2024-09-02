import pandas as pd
import numpy as np

file_path = 'D:\\7月21数据\\Flat\\London_flat.xlsx'
# we will replace flat by "detached" and "terrace" one by one
df = pd.read_excel(file_path)

# Process the 'NearestStations' column to keep only the first number in each cell
df['NearestStations'] = df['NearestStations'].str.extract(r'(\d+\.\d+)')

# Function to convert size range to average size
def convert_size(size):
    if '-' in size:
        start, end = size.replace(' sq ft', '').split('-')
        return (int(start.replace(',', '')) + int(end.replace(',', ''))) / 2
        # Beacuse some houses show a range of size like 800-900 sq ft, we try to use mean value to replace
    else:
        return int(size.replace(' sq ft', '').replace(',', ''))

# Apply the function to the 'Size' column
df['Size'] = df['Size'].apply(convert_size)

# Remove rows with any missing values
df.dropna(inplace=True)

# Save the processed DataFrame to Excel file
df.to_excel(file_path, index=False)

