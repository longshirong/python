# -*- coding:utf-8 -*-
"""
Created on 2020-7-29
@author: lori
"""

from read import readMemory
from database import TransactionManager
import pymysql

con = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='12345678',
    db='test',
    charset='utf8',
)


def upload():
    version_information = readMemory.ReadMemory().read_version()
    version = version_information[0]
    time = version_information[1]
    TransactionManager.TransactionManager.insert_into_version(con, version, time)

    logs = readMemory.ReadMemory().read_memory()
    for data in logs.iterrows():
        TransactionManager.TransactionManager.insert_into_records(con, data[1])


if __name__ == '__main__':
    upload()
