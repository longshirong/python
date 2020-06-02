import numpy as np

"""
arange()给定起始结尾步长
linspace()给定起始结尾数字个数
"""
# x1 = np.arange(1, 11, 2)
# x2 = np.linspace(1, 9, 5)
#


"""
加 减 乘 除 求幂次方 取余数
"""
# x1 = np.arange(1, 11, 2)
# x2 = np.linspace(1, 9, 5)
# print(np.add(x1, x2))
# print(np.subtract(x1, x2))
# print(np.multiply(x1, x2))
# print(np.divide(x1, x2))
# print(np.power(x1, x2))
# print(np.remainder(x1, x2))
#
"""
求整个矩阵的最小值
求矩阵每一列里的最小值最后形成一行
求矩阵每一行里的最小值最后形成一列
下面的同理可得
"""
# a = np.array([[1, 2, 3], [4, 1, 6], [7, 8, 9]])
# print(np.amin(a))
# print(np.amin(a, 0))
# print(np.amin(a, 1))
# print(np.amax(a))
# print(np.amax(a, 0))
# print(np.amax(a, 1))

"""
percentile() 代表着第 p 个百分位数，这里 p 的取值范围是 0-100，
如果 p=0，那么就是求最小值，如果 p=50 就是求平均值，如果 p=100 就是求最大值。
同样你也可以求得在 axis=0 和 axis=1 两个轴上的 p% 的百分位数。

求整个矩阵的最大差
求每一列里最大差形成一行
求每一行里的最大差形成一列
"""
# a = np.array([[1, 2, 3], [4, 1, 6], [7, 8, 9]])
# print(np.ptp(a))
# print(np.ptp(a, 0))
# print(np.ptp(a, 1))

"""
求整个矩阵的平均值
求每一列的平均值组成一行
求每一列的平均值组成一列
"""
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(np.percentile(a, 50))
# print(np.percentile(a, 50, axis=0))
# print(np.percentile(a, 50, axis=1))

"""
求整个矩阵的中位数，可以看成压缩成一行后并排好序再求中位数，并不是简单的取中间的值
求每一列排好序后的中位数并组成一行
求每一行的中位数并组成一列
下面的同理
"""

# a = np.array([[1, 2, 3], [4, 1, 6], [7, 8, 9]])
# # 求中位数
# print(np.median(a))
# print(np.median(a, axis=0))
# print(np.median(a, axis=1))
# # 求平均数
# print(np.mean(a))
# print(np.mean(a, axis=0))
# print(np.mean(a, axis=1))


"""
求数组平均值
求加权平均值(1x1+2x2+3x3+4x4)/(1+2+3+4)=3.0
"""
# a = np.array([1, 2, 3, 4])
# wts = np.array([1, 2, 3, 4])
# print(np.average(a))
# print(np.average(a, weights=wts))

"""
std标准差
var方差
"""
# a = np.array([1, 2, 3, 4])
# print(np.std(a))
# print(np.var(a))

"""
sort(a, axis=-1, kind=‘quicksort’, order=None)，默认情况下使用的是快速排序；
在 kind 里，可以指定 quicksort、mergesort、heapsort 分别表示快速排序、合并排序、堆排序。
同样 axis 默认是 -1，即沿着数组的最后一个轴进行排序，也可以取不同的 axis 轴，或者 axis=None 
代表采用扁平化的方式作为一个向量进行排序。另外 order 字段，对于结构化的数组可以指定按照某个字段进行排序。

对每一行进行排序
压缩成一维后进行排序
按照每一列进行排序
按照每一行进行排序
"""

# a = np.array([[4, 3, 2], [2, 4, 1]])
# print(np.sort(a))
# print(np.sort(a, axis=None))
# print(np.sort(a, axis=0))
# print(np.sort(a, axis=1))
