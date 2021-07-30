import os
import shapefile
import pandas as pd

# 통계청_행정동경계
shp_path = "E:/Datasets/Administrative/통계청_행정동경계_202006/Z_SOP_BND_ADM_DONG_PG.dbf"
assert os.path.exists(shp_path)

record_dicts_list = []
with shapefile.Reader(shp_path, encoding='euc-kr') as sf:
    print(sf.fields)
    for rec in sf.records():
        if rec['ADM_DR_CD'].startswith('11'):
            record_dicts_list.append(rec.as_dict())

records_df = pd.DataFrame(record_dicts_list)
print(records_df.describe())
exit(0)

duplicate_nm_df = records_df[records_df.duplicated('EMD_KOR_NM')]
# print(duplicate_nm_df)
dup_df = records_df[records_df['EMD_KOR_NM'].isin(duplicate_nm_df['EMD_KOR_NM'])]
print(dup_df)

exit(0)

# GIS_developer_대한민국최신행정구역
shp_path = "E:/Datasets/Administrative/GIS_Developer_대한민국최신행정구역/EMD_202101/TL_SCCO_EMD.dbf"
shp_path = "/home/jy/Downloads/Datasets/Administrative/GIS_Developer_대한민국최신행정구역/EMD_202101/TL_SCCO_EMD.dbf"
assert os.path.exists(shp_path)

record_dicts_list = []
with shapefile.Reader(shp_path, encoding='euc-kr') as sf:
    print(sf.fields)
    for rec in sf.records():
        if rec['EMD_CD'].startswith('11'):
            record_dicts_list.append(rec.as_dict())

records_df = pd.DataFrame(record_dicts_list)
print(records_df.describe())
exit(0)

duplicate_nm_df = records_df[records_df.duplicated('EMD_KOR_NM')]
# print(duplicate_nm_df)
dup_df = records_df[records_df['EMD_KOR_NM'].isin(duplicate_nm_df['EMD_KOR_NM'])]
print(dup_df)

