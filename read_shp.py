import os
import shapefile
import pandas as pd

# shp_path = "E:/Datasets/Administrative/GIS_Developer_대한민국최신행정구역/EMD_202101/TL_SCCO_EMD.dbf"
shp_path = "/home/jy/Downloads/Datasets/Administrative/GIS_Developer_대한민국최신행정구역/EMD_202101/TL_SCCO_EMD.dbf"
assert os.path.exists(shp_path)

record_dicts_list = []
with shapefile.Reader(shp_path, encoding='euc-kr') as sf:
    print(sf.fields)
    for rec in sf.records():
        if rec['EMD_CD'].startswith('11'):
            record_dicts_list.append(rec.as_dict())

records_df = pd.DataFrame(record_dicts_list)
duplicate_nm_df = records_df[records_df.duplicated('EMD_KOR_NM')]
# print(duplicate_nm_df)
dup_df = records_df[records_df['EMD_KOR_NM'].isin(duplicate_nm_df['EMD_KOR_NM'])]
print(dup_df)
