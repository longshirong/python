"""
为了测试读取数据是否满足要求进行的文件测试
"""
from read import readMemory

logs = readMemory.ReadMemory().read_memory()
logs.to_csv('test.txt', sep='\t', index=False)
