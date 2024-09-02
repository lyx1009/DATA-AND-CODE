import os
import pandas as pd

# 设置文件路径
folder_path = 'D:\\7月21数据\\Flat\\'
files = os.listdir(folder_path)
# Detached is 'D:\\7月21数据\\Detached\\'
# Terrace is 'D:\\7月21数据\\Terrace\\' replace

# The list of Inner and Outer London boroughs
inner_london = ['Camden', 'Greenwich', 'Hackney', 'Hammersmith and Fulham', 'Islington', 'Kensington and Chelsea',
                'Lambeth', 'Lewisham', 'Southwark', 'Tower Hamlets', 'Wandsworth', 'Westminster']
outer_london = ['Barking and Dagenham', 'Barnet', 'Bexley', 'Brent', 'Bromley', 'Croydon', 'Ealing', 'Enfield',
                'Haringey', 'Harrow', 'Havering', 'Hillingdon', 'Hounslow', 'Kingston upon Thames', 'Merton', 'Newham',
                'Redbridge', 'Richmond upon Thames', 'Sutton', 'Waltham Forest']

# set a dataframe
all_dfs = []

# Iterate over the files and classify
for file in files:
    file_path = os.path.join(folder_path, file)

    # Check if it's a file (not a directory)
    if os.path.isfile(file_path):
        borough_name = file.replace('-flat.xlsx', '')  # Extract the name of borough from the filename
        try:
            df = pd.read_excel(file_path)  # Loading excel Files

            # Create a new column based on the classification
            if borough_name in inner_london:
                df['Region'] = 'Inner London'
            elif borough_name in outer_london:
                df['Region'] = 'Outer London'

            # Add to the total data box list
            all_dfs.append(df)

        except Exception as e:
            print(f"loading {file_path} erro: {e}")
    else:
        print(f"skip: {file_path}")

# Merge all
if all_dfs:
    combined_df = pd.concat(all_dfs, ignore_index=True)
    combined_df.to_excel('D:\\7月21数据\\Flat\\London_flat.xlsx', index=False)

#Detached is 'D:\\7月21数据\\Detached\\London_detached.xlsx' 
#Terrace is 'D:\\7月21数据\\Detached\\London_terrace.xlsx' replace'

print("save as : London_flat.xlsx")
