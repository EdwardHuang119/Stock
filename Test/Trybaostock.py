# -*- coding: utf-8 -*-
import baostock as bs
import pandas as pd
import numpy as np
import tushare as ts

lg = bs.login(user_id="anonymous", password="123456")
# print(help(bs.query_history_k_data))

# field = 'date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST'
# rs = bs.query_history_k_data(code='sh.601398',fields=field,start_date='2009-01-01',end_date='2018-10-08')
#
# data_list = []
# while (rs.error_code == '0') & rs.next():    # 获取一条记录，将记录合并在一起
#     data_list.append(rs.get_row_data())
# result = pd.DataFrame(data_list, columns=rs.fields)
# print(result)

cc = ts.get_hist_data('000002','2009-01-01','2018-10-08','D')
print(type(cc),cc)

# dd = ts.get_h_data('000002','2009-01-01')
# print(dd)
# help(ts.get_h_data)
bs.logout()

