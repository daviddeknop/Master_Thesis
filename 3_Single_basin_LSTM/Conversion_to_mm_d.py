import pandas as pd

# Define the file path
file_path = r'E:\Users\ddknop\neuralhydrology_2_updated\output_caravan\timeseries\csv\6\6.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Check the first few rows of the DataFrame to understand its structure
print("Before modification:")
print(df.head())

# Assuming 'streamflow' is the name of the column to modify
# Perform the required transformation
df['streamflow'] = (df['streamflow'] / 111249644.3) * (3600 * 24 * 1000)

# Check the first few rows after modification
print("After modification:")
print(df.head())

# Get the directory of the original file to save the modified file in the same location
directory = os.path.dirname(file_path)

# Define the new file path for the modified CSV
new_file_path = os.path.join(directory, 'modified_streamflow.csv')

# Save the modified DataFrame back to the same directory
df.to_csv(new_file_path, index=False)

print(f"Modified CSV saved as: {new_file_path}")