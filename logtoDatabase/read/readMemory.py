import pandas as pd


class ReadMemory:
    def __init__(self):
        self.path = '/Users/didi/Documents/task/7.27/'

    # 读取version信息
    def read_version(self):
        # 读入txt文件，分隔符为\t,log是一个整体
        log = pd.read_table(self.path + 'log-2020-07-30.txt', sep='\t', header=None)
        log = log[0]
        version = log[0].split("=")[1]
        time = log[1][6:]
        return [version, time]

    # 读取memory信息
    def read_memory(self):
        # 读入txt文件，分隔符为\t,log是一个整体
        log = pd.read_table(self.path + 'log-2020-07-30.txt', sep='\t', header=None)
        log = log[0]

        index = ReadMemory.find_start(log)
        start = index + 3
        # 得到行数,每一行都有空格，前两行是版本号和时间
        length = log.size
        step = 3
        # 获取名字作为表头
        head = []
        for i in range(start, start + 8):
            line = log[i].strip().split(':')
            head.append(line[0])

        # 新建一个空的DataFrame用来保存数据
        logs = pd.DataFrame(columns=head)

        # 设置count，用来记录每一条有7行
        # 存储临时变量值
        temp = {}
        # 读取数据，DadaFrame只能添加series对象
        i = start
        count = 0
        while i < length:

            if count < 7:
                line = log[i].strip().split(':')
                data = line[1].strip()
                temp[head[count]] = data
                count += 1
            elif count == 7:
                line = log[i].strip().split(':')
                data = line[1].strip().split(' ')
                data = data[0]
                temp[head[count]] = data
                count += 1
            elif count == 8:
                count = 0
                i += step
                logs = logs.append(temp, ignore_index=True)
                temp = {}
            i += 1
        # 返回的信息里包含了表头，应该在插入数据的时候去掉，加表头只是为了检验数据是否保存正确
        time = ReadMemory.read_time(log, length)
        logs['time'] = time
        return logs

    # 找到有效数据的开始时间点
    @staticmethod
    def find_start(log):
        index = 0
        for i, line in enumerate(log):
            line = line.strip()
            if line[:3] == 'App':
                index = i
                break
        return index

    # 读时间
    @staticmethod
    def read_time(log, length) -> list:
        start = ReadMemory.find_start(log) - 1
        step = 12
        i = start
        temp = []
        while i < length-1:
            line = log[i].strip()[6:]
            temp.append(line)
            i += step
        return temp
