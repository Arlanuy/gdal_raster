from osgeo import gdal, ogr
import sys

raster = gdal.Open('raster_study_files/INPUT.tif')
for i in range(1, raster.RasterCount + 1):
	band = raster.GetRasterBand(i)
	print(band.GetMetadata())
	print(band.GetNoDataValue())
	print(band.GetMinimum())
	print(band.GetMaximum())
	print(band.GetScale())

drv = ogr.GetDriverByName('ESRI Shapefile')
outfile = drv.CreateDataSource('raster_study_files/polygonizedRaster.shp') 
outlayer = outfile.CreateLayer('raster_study_files/polygonized raster', srs = None )
newField = ogr.FieldDefn('DN', ogr.OFTReal)
outlayer.CreateField(newField)

gdal.Polygonize(band, None, outlayer, 0, [])
outfile = None 

