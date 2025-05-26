import os
from pathlib import Path
import shutil

# Get current working directory and its parent
pad = Path(os.getcwd())
parent = pad.parent

# Create necessary target directories
forcings_dir = parent / "data" / "Zwalm_data" / "preprocess_output"
qdata_dir = parent / "data" / "Zwalm_data" / "output_Q"
forcings_dir.mkdir(parents=True, exist_ok=True)
qdata_dir.mkdir(parents=True, exist_ok=True)

# Create a temporary download folder in the parent directory
temp_download_folder = parent / "temp_zenodo_download"
temp_download_folder.mkdir(parents=True, exist_ok=True)

# Download the files into the temp folder
os.system(f'zenodo_get -o "{temp_download_folder}" 10.5281/zenodo.15519122')

# Move specific files to desired target locations
for file in temp_download_folder.glob("*.pkl"):
    if "Forcings" in file.name:
        shutil.move(str(file), forcings_dir / "Final_Forcings_PDM.pkl")
        print(f"Moved {file.name} -> {forcings_dir / 'Final_Forcings_PDM.pkl'}")
    elif "Q" in file.name:
        shutil.move(str(file), qdata_dir / "Q_data.pkl")
        print(f"Moved {file.name} -> {qdata_dir / 'Q_data.pkl'}")

# Optionally remove the temp download folder
shutil.rmtree(temp_download_folder)
