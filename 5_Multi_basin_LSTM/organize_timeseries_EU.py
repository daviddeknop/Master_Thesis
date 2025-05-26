import os
import shutil
from pathlib import Path
# Pad naar de folder met de bestanden
source_folder = Path('output_caravan_EU/timeseries/netcdf/lamah') 

def organize_nc_files(source_folder):
    # Loop door alle bestanden in de folder
    for file_name in os.listdir(source_folder):
        # Controleer of het bestand eindigt op ".nc" en begint met "camels_"
        if file_name.startswith("lamah_") and file_name.endswith(".nc"):
            # Haal het serienummer uit de bestandsnaam
            series_number = file_name.split("_")[1].split(".")[0]

            # Maak een nieuwe folder gebaseerd op het serienummer
            new_folder = os.path.join(source_folder, series_number)
            os.makedirs(new_folder, exist_ok=True)

            # Stel de nieuwe bestandsnaam in
            new_file_name = f"{series_number}.nc"
            new_file_path = os.path.join(new_folder, new_file_name)

            # Verplaats en hernoem het bestand
            shutil.move(os.path.join(source_folder, file_name), new_file_path)

    print("Bestanden zijn georganiseerd!")

# Roep de functie aan
organize_nc_files(source_folder)
