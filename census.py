import numpy as np
import pandas as pd
import os

dir_name = 'E:/'
# dir_name = '/home/jy/Downloads'
src_file_path = os.path.join(dir_name, 'Datasets/Administrative/행안부/행안부인구/202106_202106_연령별인구현황_월간.csv')
dst_file_path = os.path.join(dir_name, 'Datasets/Administrative/행안부/행안부인구/202106_202106_연령별인구현황_월간_extr.csv')
census_df = pd.read_csv(src_file_path, encoding='euc-kr')

# The first 14 columns selected
census_df_sub = census_df.iloc[:, list(range(14))]
# Rename the columns
col_name = ['Adm_Div', 'Total', 'Total2', 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
census_df_sub.columns = col_name
# 'Total2' dropped, because it is a duplicate of 'Total'
census_df_sub = census_df_sub.drop('Total2', axis=1)

# Splitting Adm_Div
# 'Adm_Div': 서울특별시... (code 10 digits)
# using str.extract
admdiv_regex = "(?P<SIDO>[가-햫]+)\s(?P<EMD>[^()]+)\((?P<EMD_CODE>\d+)00\)"
admdiv_df = census_df_sub['Adm_Div'].str.extract(admdiv_regex, expand=True)
# concat
census_df_admdiv = pd.concat([census_df_sub, admdiv_df], axis=1)
# filtering headers like 시, 구
census_df_final = census_df_admdiv[census_df_admdiv['EMD'].str.split().str.len() > 1]
census_df_final = census_df_final.drop('Adm_Div', axis=1)

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# census_df_sub = census_df.loc[:, ['EMD_CD', 'Total_Living_Pop']]
grouped = census_df_final.groupby(by='SIDO')
# print(grouped.count())
print(grouped.get_group('서울특별시').describe())

# Save
census_df_final.to_csv(dst_file_path, index=False, encoding='euc-kr')
