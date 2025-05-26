import os
from pathlib import Path
import py7zr
import shutil

pad = Path(os.getcwd())
parent = pad.parent

temp_download_folder = parent / "temp_zenodo_download"
temp_download_folder.mkdir(parents=True, exist_ok=True)

# Use zenodo_get Python API instead of os.system for better control

os.system(f'zenodo_get -o "{temp_download_folder}" 10.5281/zenodo.15519379')



# Extract all .7z files found in the temp folder directly to the parent directory
for archive_path in temp_download_folder.glob("*.7z"):
    with py7zr.SevenZipFile(archive_path, mode='r') as archive:
        archive.extractall(path=parent)
    print(f"Extracted: {archive_path.name} -> {parent}")

# Clean up
shutil.rmtree(temp_download_folder)