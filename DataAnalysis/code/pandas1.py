import pandas as pd
import numpy as np

# x1 = pd.Series([1,2,3,4])
# x2 = pd.Series(data=[1,2,3,4], index=['a', 'b', 'c', 'd'])
#
# print(x1)
# print(x2)


# d = {'a':1, 'b':2, 'c':3, 'd':4}
# x3 = pd.Series(d)
# print(x3)


# data = {'Chinese': [66, 95, 93, 90, 80], 'English': [65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
# df1 = pd.DataFrame(data)
# df2 = pd.DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
#                    columns=['English', 'Math', 'Chinese'])
# print(df1)
# print(df2)

"""
读取excel文件，换自己的文件路径
"""
# score = pd.DataFrame(pd.read_excel('data.xlsx'))
# score.to_excel('data1.xlsx')
# print(score)


data = {'Chinese': [66, 95, 93, 90, 80], 'English': [65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
df2 = pd.DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
                   columns=['English', 'Math', 'Chinese'])

# # 删除某一列
# df2 = df2.drop(columns=['Chinese'])
# # 删除某一行
# df2 = df2.drop(index=['ZhangFei'])
# # 对某些列进行换名字
# df2.rename(columns={'Chinese': 'YuWen', 'English': 'Yingyu'}, inplace=True)
# #  去除重复行
# df = df2.drop_duplicates()
# # 更改数据类型
# df2['Chinese'].astype('str')
# df2['Chinese'].astype(np.int64)
#
# # 删除左右两边空格
# df2['Chinese'] = df2['Chinese'].map(str.strip)
# # 删除左边空格
# df2['Chinese'] = df2['Chinese'].map(str.lstrip)
# # 删除右边空格
# df2['Chinese'] = df2['Chinese'].map(str.rstrip)
# # 删除特殊符号
# df2['Chinese'] = df2['Chinese'].str.strip('$')
#
# # 全部大写
# df2.columns = df2.columns.str.upper()
# # 全部小写
# df2.columns = df2.columns.str.lower()
# # 首字母大写
# df2.columns = df2.columns.str.title()
# # 查找空格
# df = df2.isnull().any()
# # name列都转化为大写
# df2['name'] = df2['name'].apply(str.upper)


# def double_df(x):
#     return 2 * x
#
#
# df2[u'Chinese'] = df2[u'Chinese'].apply(double_df)
# print(df2)

"""
其中 axis=1 代表按照列为轴进行操作，axis=0 代表按照行为轴进行操作，
args 是传递的两个参数，即 n=2, m=3，在 plus 函数中使用到了 n 和 m，从而生成新的 df。
"""


# def plus(df, n, m):
#     df['new1'] = (df[u'Chinese'] + df[u'English']) * m
#     df['new2'] = (df[u'Chinese'] + df[u'English']) * n
#     return df
#
#
# df2 = df2.apply(plus, axis=1, args=(2, 3,))


# df1 = pd.DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
# print(df1)
# print(df1.describe())


# df1 = pd.DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
# df2 = pd.DataFrame({'name':['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data2':range(5)})
# # 指定列连接
# df3 = pd.merge(df1, df2, on='name')
# # 内连接，这里还是依据name连接，求交集
# df3 = pd.merge(df1, df2, how='inner')
# # 左连接，类比SQL，左满不相交的为空值并显示出来
# df3 = pd.merge(df1, df2, how='left')
# # 右连接，类比SQL，右满，不相交的为空值并显示出来
# df3 = pd.merge(df1, df2, how='right')
# #　外连接，类比SQL里的，左满右满，不相交为空值，并显示出来，相当于求并
# df3 = pd.merge(df1, df2, how='outer')
# print(df3)


# import pandas as pd
# from pandas import DataFrame
# from pandasql import sqldf, load_meat, load_births
df1 = pd.DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
# pysqldf = lambda sql: sqldf(sql, globals())
# sql = "select * from df1 where name ='ZhangFei'"
# print pysqldf(sql)
print(df1.iloc[0:1])