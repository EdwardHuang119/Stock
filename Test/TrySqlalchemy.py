#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, event,MetaData,Table
# from sqlalchemy import *
import pymysql

engine = create_engine('mysql+pymysql://root:3621@(!@cdb-91rtu6jl.gz.tencentcdb.com:10045/Stock_test?charset=utf8')
conn = engine.connect()
# metadata = MetaData(engine)

# def serch():
#     table = Table('Stock_basic', metadata, autoload=True)
#     s = select([table])
#     conn.execute(s)



