import geopandas as gpd
import pandas as pd 
from pathlib import Path
import os
import matplotlib.pyplot as plt

# Set the working directory
path = Path(os.getcwd())

# Read the shapefile into a GeoDataFrame
allriv = gpd.read_file(path / "data_Flanders/AfstrZonA0.shp")
mask = allriv['A0NAAM'].str.contains('bellebeek', case=False, na=False)
rownr = allriv.index[mask].tolist()
Bellebeek_gpd = allriv.loc[rownr]
Bellebeek_gpd.rename(columns={'BEKNR': 'gauge_id'}, inplace=True)

# Create the output directory if it doesn't exist
if not os.path.exists('data/Bellebeek_shape'):
    os.makedirs('data/Bellebeek_shape')

# Save the combined geometry as a shapefile in Lambert 72
lambert_shapefile_path = Path( path / "data/Bellebeek_shape/Bellebeek_shapefile_31370.shp")
Bellebeek_gpd.to_file(lambert_shapefile_path)
print(f"Shapefile saved in Lambert 72: {lambert_shapefile_path}")

# Convert the geometry to WGS 84 (EPSG: 4326)
Bellebeek_gpd = Bellebeek_gpd.to_crs(epsg=4326) 


wgs84_shapefile_path = Path(path / "data/Bellebeek_shape/Bellebeek_shapefile_4326.shp")
Bellebeek_gpd.to_file(wgs84_shapefile_path)
print(f"Shapefile saved in WGS 84: {wgs84_shapefile_path}")

# Visualize the shapefile
Bellebeek_gpd.plot(figsize=(10, 6), color="blue", edgecolor="black")
plt.title("Bellebeek River - WGS 84 Projection")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.show()

