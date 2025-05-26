import os
from pathlib import Path
import zipfile
import shutil

# Get current working directory and its parent
pad = Path(os.getcwd())
parent = pad.parent

# Create a temporary download folder in the parent directory
temp_download_folder = parent / "temp_zenodo_download"
temp_download_folder.mkdir(parents=True, exist_ok=True)

# Download the ZIP file into the temp folder
os.system(f'zenodo_get -o "{temp_download_folder}" 10.5281/zenodo.15518784')

# Extract all ZIP files found in the temp folder directly to the parent directory
for zip_path in temp_download_folder.glob("*.zip"):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(parent)
    print(f"Extracted: {zip_path.name} -> {parent}")

# Optionally remove the temp download folder
shutil.rmtree(temp_download_folder)

