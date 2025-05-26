
import os
from pathlib import Path
import zipfile
import shutil

# Define paths
pad = Path(os.getcwd())
parent = pad.parent

temp_download_folder = parent / "temp_zenodo_download"
temp_download_folder.mkdir(parents=True, exist_ok=True)

# Download dataset using zenodo_get
os.system(f'zenodo_get -o "{temp_download_folder}" 10.5281/zenodo.15521646')

# Extract all .zip files found in the temp folder directly to the parent directory
for archive_path in temp_download_folder.glob("*.zip"):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(path=parent)
    print(f"Extracted: {archive_path.name} -> {parent}")

# Clean up
shutil.rmtree(temp_download_folder)


#experiment for filtered

import os
from pathlib import Path
import zipfile
import shutil

# Define paths
pad = Path(os.getcwd())
parent = pad.parent

temp_download_folder = parent / "temp_zenodo_download"
temp_download_folder.mkdir(parents=True, exist_ok=True)

# Download dataset using zenodo_get
os.system(f'zenodo_get -o "{temp_download_folder}" 10.5281/zenodo.15521819')

# Extract all .zip files found in the temp folder directly to the parent directory
for archive_path in temp_download_folder.glob("*.zip"):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(path=parent)
    print(f"Extracted: {archive_path.name} -> {parent}")

# Clean up
shutil.rmtree(temp_download_folder)
