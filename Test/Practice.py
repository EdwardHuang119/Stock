# -*- coding: utf-8 -*-
import platform

systemtype = platform.system()
if systemtype == 'Windows':
    print('a')
else:
    print('b')