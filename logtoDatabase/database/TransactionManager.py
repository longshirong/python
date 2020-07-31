# -*- coding:utf-8 -*-
"""
Created on 2020-7-29
@author: lori
"""
import re


# 变量初始化
class TransactionManager(object):

    # 插入版本表和数据表
    def insert(self, version_information: list, memory_information: list):
        version = version_information[0]
        time = version_information[1]
        TransactionManager.insert_into_version(self, version, time)
        for line in memory_information:
            memory = re.split(r'\t|\n', line)
        TransactionManager.insert_into_records(self, memory)

    # 定义软删除的字段status，初始化为1
    @staticmethod
    def insert_into_version(con, version_name: str, time_stamp: str):
        cue = con.cursor()

        status = 1
        try:
            cue.execute(
                "insert into version(versionName, status, time_stamp) values(%s,%s,%s)",
                [version_name, status, time_stamp])
        except Exception as e:
            print('Insert error:', e)
            con.rollback()
        else:
            con.commit()

    @staticmethod
    def insert_into_records(con, memory):
        java_heap = memory['Java Heap']
        native_heap = memory['Native Heap']
        code = memory['Code']
        stack = memory['Stack']
        graphics = memory['Graphics']
        private_other = memory['Private Other']
        system = memory['System']
        total = memory['TOTAL']
        time = memory['time']

        cue = con.cursor()
        try:
            num = cue.execute("select id from version")
        except Exception as e:
            print('get id error', e)
            con.rolback()
        else:
            con.commit()

        try:
            cue.execute(
                "insert into records(JavaHeap, NativeHeap, Codes, Stack, Graphics, PrivateOther, Systems, TOTAL, version_id, time)"
                " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                [java_heap, native_heap, code, stack, graphics, private_other, system, total, num, time])
        except Exception as e:
            print('Insert error:', e)
            con.rollback()
        else:
            con.commit()
