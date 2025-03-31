import pandas as pd

# 1. 分别读取三个文件
df1 = pd.read_csv("accidents_2005_to_2007.csv")
df2 = pd.read_csv("accidents_2009_to_2011.csv")
df3 = pd.read_csv("accidents_2012_to_2014.csv")

# 2. 垂直合并数据（确保列名一致）
merged_df = pd.concat([df1, df2, df3], axis=0)

# 3. 保存为完整文件
merged_df.to_csv("Accidents_2005_to_2014.csv", index=False)


