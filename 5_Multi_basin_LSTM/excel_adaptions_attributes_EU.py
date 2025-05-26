import pandas as pd
import os
from pathlib import Path

# Read the original CSV file
input_file = Path('output_caravan_EU/attributes/attributes.csv') # Replace with your actual file path
df = pd.read_csv(input_file, dtype=str)  # Ensure the data is read as strings to preserve leading zeros
df['gauge_id'] = df['gauge_id'].str.split('_').str[1]
df.to_csv(input_file, index=False)
# Set base output path where the folders should be created
base_output_path = Path('output_caravan_EU/attributes')
df = pd.read_csv(input_file, dtype=str) 
# Iterate over each row of the first column
for index, row in df.iterrows():
    # Get the series number (first column value)
    series_number = row[0]  # Assumes the first column contains the series number
    
    # Create a folder named after the full series number inside the specified base directory
    folder_name = os.path.join(base_output_path, f'{series_number}')
    
    # Create the directory if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Create a new DataFrame with only the current row (including the header)
    new_df = df.iloc[[index]]  # Select the row with the header included
    
    # Save the row into a new CSV file in the appropriate folder with header
    output_file = os.path.join(folder_name, f'{series_number}.csv')
    
    # Save the CSV file with the first column as text
    new_df.to_csv(output_file, index=False, header=True, na_rep='')  # Set header=True to include the header

print("CSV files created successfully with headers!")
