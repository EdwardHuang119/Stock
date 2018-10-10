#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

# help(pymysql.connect)

def connect_db():
    """Connect database and return db and cursor"""
    db = pymysql.connect(host="cdb-91rtu6jl.gz.tencentcdb.com",port=10045,user='root',
                         passwd='3621@(!jj',db="Stock_test")
    cursor = db.cursor()
    return (db,cursor)

db,cursor = connect_db()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)
db.close()