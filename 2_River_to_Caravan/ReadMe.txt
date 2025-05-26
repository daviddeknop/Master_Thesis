Caravan_part1_Earth_Engine.ipynb and Caravan_part2_local_postprocessing.ipynb are an adapted version of Kratzert notebook for conversion of Flanders catchments into Caravan format.
Note that the first notebook should be exicuted in google Colab to ensure access to google Earth Engine.

Before running these notebooks, the shp, dbf and shx from step 1 has to be uploaded in the google Earth Engine as a new asset. After this the notebooks can be followed.
The output is stored in output_caravan.

For the second notebook conversion of coordinates are needed to transform the Lambert 72 coordinates into WGS-84, therefor the script conversion_coordinates.py need to be runed 
note that conversion of coordinates is not part of the neuralhydrology environment. Run this in the thesis environment.