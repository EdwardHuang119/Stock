#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
import os
from configparser import ConfigParser

# help(pymysql.connect)

# fatherpath = os.getcwd()
configname = 'config.conf'
fatherpath = os.path.abspath(os.path.dirname(os.getcwd()))
configpath = fatherpath+'confing'+'//'+configname
cf = ConfigParser()
cf.read(configpath)

a = cf.read()

# host = cf.get("tencentcdb","host")
# /Users/Mac/PycharmProjects/Stock/confing

print(a)


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