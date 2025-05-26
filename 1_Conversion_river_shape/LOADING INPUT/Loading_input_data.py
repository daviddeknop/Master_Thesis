import os
from pathlib import Path
import zipfile

# Get current working directory and its parent
pad = Path(os.getcwd())
parent = pad.parent

# Create output folder in the parent directory
output_folder = parent / "data_Flanders"
output_folder.mkdir(parents=True, exist_ok=True)

# Download the files using zenodo_get into the output folder
os.system(f"zenodo_get -o \"{output_folder}\" 10.5281/zenodo.15518099")

# Unzip all ZIP files found in the downloaded folder
for zip_path in output_folder.glob("*.zip"):
    extract_folder = output_folder / zip_path.stem
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Extracted: {zip_path.name} -> {extract_folder}")
