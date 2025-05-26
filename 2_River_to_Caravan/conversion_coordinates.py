import pyproj

# Define the EPSG code for the Belgian Lambert 2008
lambert_epsg = 31370 

# Create a transformer object
# The EPSG code for WGS84 is 4326
transformer = pyproj.Transformer.from_crs(lambert_epsg, 4326, always_xy=True)

# Station easting and northing values (example values)
easting_zwalm = 101966.00  # Replace with actual easting value
northing_zwalm = 175227.00  # Replace with actual northing value
easting_bellebeek = 132234.00
northing_bellebeek = 175407.00
# Transform the coordinates
longitude_zwalm, latitude_zwalm = transformer.transform(easting_zwalm, northing_zwalm)
longitude_bellebeek, latitude_bellebeek = transformer.transform(easting_bellebeek, northing_bellebeek)
# Print the results
print(f"WGS84 Coordinates Zwalm: Latitude: {latitude_zwalm}, Longitude: {longitude_zwalm}")
print(f"WGS84 Coordinates Bellebeek: Latitude: {latitude_bellebeek}, Longitude: {longitude_bellebeek}")