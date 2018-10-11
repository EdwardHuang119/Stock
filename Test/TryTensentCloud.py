#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
import os
from configparser import ConfigParser


# 读取配置文件处理
configname = 'config.conf'
fatherpath = os.path.abspath(os.path.dirname(os.getcwd()))
configpath = fatherpath+'\\confing'+'\\'+configname
cf = ConfigParser()
cf.read(configpath)
host = cf.get("tencentcdb","host")
port = int(cf.get("tencentcdb","port"))
user = cf.get("tencentcdb","user")
passwd = cf.get("tencentcdb","passwd")
dba = cf.get("tencentcdb","db")


def connect_db():
    """Connect database and return db and cursor"""
    db = pymysql.connect(host=host,port=port,user=user,
                         passwd=passwd,db=dba)
    cursor = db.cursor()
    return (db,cursor)

db,cursor = connect_db()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)
db.close()


# def connect_db():
#     """Connect database and return db and cursor"""
#     db = pymysql.connect(host="cdb-91rtu6jl.gz.tencentcdb.com",port=10045,user='root',
#                          passwd='3621@(!jj',db="Stock_test")
#     cursor = db.cursor()
#     return (db,cursor)
#
# db,cursor = connect_db()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print("Database version : %s " % data)
# db.close()