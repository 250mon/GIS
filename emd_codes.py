import os
import pandas as pd
import read_shp


# dir_name = "E:/"
# dir_name = "/home/jy/Downloads/"
dir_name = "C:/Users/idiot/Documents/sjy"

# Adm_Div DB of shapefile
shp_file = "Datasets/PublicDataPortal/Administrative/법정구역정보/AL_00_D001_20210703_EMD/AL_00_D001_20210703(EMD).dbf"
shp_path = os.path.join(dir_name, shp_file)
dong_by_law_df = read_shp.read_shp(shp_path)

# census CSV file
census_file = "Datasets/PublicDataPortal/Administrative/행안부/행안부인구/202106_202106_연령별인구현황_월간.csv"
census_path = os.path.join(dir_name, census_file)
census_df = pd.read_csv(census_path, encoding='euc-kr')

# mapping CSV file
mapping_file = "Datasets\PublicDataPortal\Administrative\행안부\Codes\jscode20210705(말소코드포함)\KIKmix.20210705(말소코드포함).xlsx"
mapping_path = os.path.join(dir_name, mapping_file)
mapping_df = pd.read_excel(mapping_path) #,  encoding='euc-kr')

# print(dong_by_law_df.head(5))
# print(census_df.head(5))
print(mapping_df.head(5))
