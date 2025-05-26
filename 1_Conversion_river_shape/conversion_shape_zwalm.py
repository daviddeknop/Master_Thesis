import geopandas as gpd
import pandas as pd  
from pathlib import Path
import os
import zipfile
import matplotlib.pyplot as plt

# Set the working directory
path = Path(os.getcwd())

# Read the shapefile into a GeoDataFrame
allriv = gpd.read_file(path / "data_Flanders/AfstrZonA0.shp")
mask = allriv['A0NAAM'].str.contains('Zwalm', case=False, na = False)
rownr = allriv.index[mask].tolist()
zwalm_gpd = allriv.loc[rownr]
zwalm_gpd.rename(columns={'BEKNR' : 'gauge_id'}, inplace = True)




# Create the output directory if it doesn't exist
if not os.path.exists('data/Zwalm_shape'):
    os.makedirs('data/Zwalm_shape')

# Save the combined geometry as a shapefile in Lambert 72
Lambert_72_path = Path(path / "data/Zwalm_shape/zwalm_shapefile_31370.shp")
zwalm_gpd.to_file(Lambert_72_path)
print(f"Shapefile saved in Lambert 72: {Lambert_72_path}")

# Convert the geometry to WGS 84 (EPSG: 4326)
zwalm_gpd['geometry'] = zwalm_gpd['geometry'].to_crs(epsg=4326)


# Save the combined geometry as a shapefile in WGS 84
wgs84_shapefile_path = Path(path / "data/Zwalm_shape/zwalm_shapefile_4326.shp")
zwalm_gpd.to_file(wgs84_shapefile_path)
print(f"Shapefile saved in WGS 84: {wgs84_shapefile_path}")

# Load the shapefile
shapefile_path = path / "data/Zwalm_shape/zwalm_shapefile_4326.shp" 
gdf = gpd.read_file(shapefile_path)

# Plot the shapefile
fig, ax = plt.subplots(figsize=(10, 8))
gdf.plot(ax=ax, color='lightblue', edgecolor='black')

# Add title and labels

ax.set_xlabel("Longitude", fontsize=12)
ax.set_ylabel("Latitude", fontsize=12)

# Show the plot
plt.show()



