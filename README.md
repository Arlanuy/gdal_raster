# gdal_raster
The raster process of three different 3 tiff files and merging such bands with corresponding metadata to form a raster array

The metadata includes array_rows, array_cols, bands, driver, projection, geotransform, pixelwidth/height, nodatavalue, scalefactor.
The database is just a blob of the 3 different input tiff files and we connect this dataset to gdal in order to form an array of rasters.
