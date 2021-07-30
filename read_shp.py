import os
import shapefile
import pandas as pd


def read_shp(shp_path):
    """Read a shape file and returns a data frame"""
    assert os.path.exists(shp_path)

    record_dicts_list = []
    with shapefile.Reader(shp_path, encoding='euc-kr') as sf:
        print(sf.fields)
        for rec in sf.records():
            record_dicts_list.append(rec.as_dict())

    records_df = pd.DataFrame(record_dicts_list)
    return records_df


if __name__ == "__main__":
    # dir_name = "E:/"
    # dir_name = "/home/jy/Downloads/"
    dir_name = "C:/Users/idiot/Documents/sjy"

    # file_name = "Datasets/Administrative/GIS_Developer_대한민국최신행정구역/EMD_202101/TL_SCCO_EMD.dbf"
    file_name = "Datasets\PublicDataPortal\Administrative\법정구역정보\AL_00_D001_20210703_EMD\AL_00_D001_20210703(EMD).dbf"

    shp_path = os.path.join(dir_name, file_name)
    records_df = read_shp(shp_path)
    # looking for a duplicate records
    duplicate_nm_df = records_df[records_df.duplicated('EMD_KOR_NM')]
    # print(duplicate_nm_df)
    dup_df = records_df[records_df['EMD_KOR_NM'].isin(duplicate_nm_df['EMD_KOR_NM'])]
    print(dup_df)
