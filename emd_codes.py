import os
import pandas as pd
import read_shp


# Adm_Div DB of shapefile
# dir_name = "E:/"
# dir_name = "/home/jy/Downloads/"
dir_name = "C:/Users/idiot/Documents/sjy"

# file_name = "Datasets/Administrative/GIS_Developer_대한민국최신행정구역/EMD_202101/TL_SCCO_EMD.dbf"
file_name = "Datasets\PublicDataPortal\Administrative\법정구역정보\AL_00_D001_20210703_EMD\AL_00_D001_20210703(EMD).dbf"

shp_path = os.path.join(dir_name, file_name)
dong_by_law_df = read_shp.read_shp(shp_path)

# census CSV file
