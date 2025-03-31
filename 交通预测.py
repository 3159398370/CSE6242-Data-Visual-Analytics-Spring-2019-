import pandas as pd
import numpy as np

# 读取合并后的文件（无需指定dtype）
df = pd.read_csv("Accidents_2005_to_2014.csv")

# 验证数据
print(df.head())  # 查看前5行数据
print(df.shape)   # 查看总行数和列数
# 打印数据框的列名
print(df.columns)

# 创建一个新的DataFrame，只包含原始DataFrame中的'Location_Easting_OSGR'和'Location_Northing_OSGR'两列
new_accidents_file = df[['Location_Easting_OSGR', 'Location_Northing_OSGR']].copy()

# 打印新的DataFrame的前5行
print(new_accidents_file.head(5))

# 将新的DataFrame保存为csv文件
new_accidents_file.to_csv('Accident_Coords_2005_to_2014.csv')

# 读取Accidents_2005_to_2014.csv文件，并将数据类型设置为unicode
df = pd.read_csv('Accidents_2005_to_2014.csv', dtype='unicode')
# 读取Accidents0514andLatLon.csv文件，并将数据类型设置为unicode
df_coords = pd.read_csv('Accidents0514andLatLon.csv', dtype='unicode')

print(df_coords.columns)


df['Lat'] = df_coords['Lat']
df['Lon'] = df_coords['Lon']
df.to_csv('Accident_2005_to_2014_ll.csv')

import pandas as pd
df = pd.read_csv('Accidents_2005_to_2014.csv', dtype='unicode')
# 提取日期中的年份，并将其作为新的列'Year'添加到DataFrame中
df['Year'] = df['Date'].str[6:10]

print(df.columns)