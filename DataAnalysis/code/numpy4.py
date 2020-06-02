import numpy as np

"""
S32不支持中文
U10支持中文
"""
# 定义数据类型
persontype = np.dtype({
    'names': ['name', 'chinese', 'english', 'math'],
    'formats': ['U10', 'i', 'i', 'i']})

peoples = np.array([("张飞", 66, 65, 30), ("关羽", 95, 85, 98),
                    ("赵云", 93, 92, 96), ("黄忠", 90, 88, 77),
                    ("马超", 80, 90, 90)], dtype=persontype)
# 指定的竖列
name = peoples[:]['name']
chinese = peoples[:]['chinese']
english = peoples[:]['english']
math = peoples[:]['math']


# 定义函数用于显示每一排的内容
def show(na, cj):
    print('{} | {} | {} | {} | {} | {} '
          .format(na, np.mean(cj), np.min(cj), np.max(cj), np.var(cj), np.std(cj)))


print("科目 | 平均成绩 | 最小成绩 | 最大成绩 | 方差 | 标准差")
show("语文", chinese)
show("英语", english)
show("数学", math)

print("排名:")
# 用sorted函数进行排序
ranking = sorted(peoples, key=lambda x: x[1] + x[2] + x[3], reverse=True)
print(ranking)
