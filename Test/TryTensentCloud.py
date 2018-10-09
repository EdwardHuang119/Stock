#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
import time
import tencentcloud as QQ

QQ.__version__

# def connect_db():
#     """Connect database and return db and cursor"""
#     db = pymysql.connect(host="cdb-86podtot.gz.tencentcdb.com:10016",user='root',
#                          passwd='secret227@@&',db="cdb210819")
#     cursor = db.cursor()
#     return (db,cursor)
#
# db,cursor = connect_db()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print("Database version : %s " % data)
# # db.close()