import os
import shapefile

shp_path = "E:/Datasets/Administrative/GIS_Developer_대한민국최신행정구역/EMD_202101/TL_SCCO_EMD.dbf"
assert os.path.exists(shp_path)

with shapefile.Reader(shp_path) as shpfile:
