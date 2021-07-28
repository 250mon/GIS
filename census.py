import numpy as np
import pandas as pd
import os

dir_name = 'E:/Datasets/PeopleDong'
src_file_path = 'E:/Datasets/Administrative/행안부/행안부인구/202106_202106_연령별인구현황_월간.csv'
dst_file_path = 'E:/Datasets/Administrative/행안부/행안부인구/202106_202106_연령별인구현황_월간_extr.csv'
census_df = pd.read_csv(src_file_path, encoding='euc-kr')

# The first 14 columns selected
census_df_sub = census_df.iloc[:, list(range(14))]
# Rename the columns
col_name = ['Adm_Div', 'Total', 'Total2', 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
census_df_sub.columns = col_name
# 'Total2' dropped, because it is a duplicate of 'Total'
census_df_final = census_df_sub.drop('Total2', axis=1)
# 'Adm_Div': 서울특별시... (code 10 digits)
import re
def get_code(str_code):
    code_regex = re.compile(r'([^()]+)\((\d+)00\)')
    adm_div_gprs = code_regex.search(str_code)
    return adm_div_gprs.group(2)

# census_df_final = census_df_sub2.iloc[:, [0]].apply(get_code): not working
# because it works like get_code(Series)
census_df_final['EMD_CODE'] = census_df_final.iloc[:, 0].apply(get_code)
census_df_final = census_df_final.drop('Adm_Div', axis=1)

census_df_final.to_csv(dst_file_path, index=False, encoding='euc-kr')

# pd.set_option('display.max_columns', None)
# census_df_sub = census_df.loc[:, ['EMD_CD', 'Total_Living_Pop']]
# print(census_df_sub.groupby(by='EMD_CD').describe())

