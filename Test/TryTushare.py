#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tushare as ts

print(ts.__version__)

# ICBC = tushare.get_k_data(code='601398',start='20180101',end='20181008',ktype='D')
ICBC = ts.get_k_data('601398',start='2018-01-01',end='2018-10-08',ktype='D')

# print(ts.top_list('2010-01-19'))
# print(ts.get_k_data())
print(ICBC)

# help()