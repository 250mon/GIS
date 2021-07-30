import os
import shapefile
import sys


def browse_shp(shp_path):
    record_dicts_list = []
    with shapefile.Reader(shp_path, encoding='euc-kr') as sf:
        print(sf.fields)
        for i, rec in enumerate(sf.records()):
            print(rec)
            if i > 2:
                break


if __name__ == '__main__':
    dir_name = "C:/Users/idiot/Documents/sjy"
    # file_path = os.path.join(dir_name, "Datasets\PublicDataPortal\Administrative\GIS_Developer_대한민국최신행정구역\EMD_202101\TL_SCCO_EMD.dbf")
    file_path = os.path.join(dir_name, "Datasets\PublicDataPortal\Administrative\법정구역정보\AL_00_D001_20210703_EMD\AL_00_D001_20210703(EMD).dbf")
    browse_shp(file_path)
    assert os.path.exists(file_path)
    exit(0)

    shp_path = sys.argv.pop(1)
    assert os.path.exists(shp_path)
    browse_shp(shp_path)
