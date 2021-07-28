import numpy as np
import pandas as pd
import os


# read a file of market area revenue
dir_name = "E:/Datasets/상권분석/상권-추정매출/서울시 우리마을가게 상권분석서비스(상권-추정매출)_2020"
src_file = os.path.join(dir_name, "서울시우리마을가게상권분석서비스(상권-추정매출)_2020.csv")
revenue_raw = pd.read_csv(src_file, encoding="euc-kr")
# print(revenue_raw.head(5))

# select only 1Q
# rev_by_q = revenue_raw.groupby('기준_분기_코드')
# rev_1q = rev_by_q.get_group(1)
# print(rev_1q)

# select only clinic data in market
rev_clinic = revenue_raw.query('서비스_업종_코드 == "CS200006"')
# select just a few columns of importance, like 분기당_매출_금액, 점포수...
rev_clinic_sub = rev_clinic.iloc[:, [0, 1, 4, 5, 6, 7, 8, 79]]
rev_avg = rev_clinic_sub.loc[:, '분기당_매출_금액'] / rev_clinic_sub.loc[:, '점포수']


# def format(x):
#     return "{:,.0f}".format(x)

# rev_avg = rev_avg.apply(format)
rev_clinic_sub.loc[:, 'avg_rev_per_clinic'] = rev_avg


# print(rev_clinic_sub)
target_csv = os.path.join(dir_name, "area_revenue.csv")
rev_clinic_sub.to_csv(target_csv, encoding='euc-kr')
