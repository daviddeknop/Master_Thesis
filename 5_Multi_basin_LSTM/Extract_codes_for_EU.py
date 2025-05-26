import os
from pathlib import Path

# Folder containing the files
folder_path = Path('output_caravan_EU/timeseries/csv/lamah')   # Replace with the path to your folder
output_file = "Traindata_without_zwalm_EU.txt"  # File for 85% of the numbers

# List to store the number series
number_series = []

# Loop through the files in the folder
for file_name in os.listdir(folder_path):
    # Check if the file matches the naming pattern
    if file_name.startswith("lamah_") and file_name.endswith(".csv"):
        # Extract the number series
        number = file_name.split("_")[1].split(".")[0]
        print(number)
        number_series.append(number)


print(number_series)

with open(output_file, "w") as f:
    for number in number_series:
        f.write(f"{number}\n")



print(f"numbers saved to {output_file}")

