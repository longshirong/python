#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 首先导入PyMySQL库
import pymysql

# 连接数据库，创建连接对象connection
# 连接对象作用是：连接数据库、发送数据库信息、处理回滚操作（查询中断时，数据库回到最初状态）、创建新的光标对象
connection = pymysql.connect(host='localhost',  # host属性
                             user='root',  # 用户名
                             password='12345678',  # 此处填登录数据库的密码
                             db='test'  # 数据库名
                             )
