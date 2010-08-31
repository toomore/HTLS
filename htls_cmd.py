#!/usr/bin/env python
# -*- coding: utf-8 -*-
import htls
from datetime import datetime
while True:
  print '結束請按 Ctrl + c\n'
  try:
    name = raw_input('請輸入姓名：')
    age = raw_input('請輸入年齡：')
    year = raw_input('請輸入年度（民國）：')

    if len(year):
      year = int(year)
    else:
      year = datetime.today().year - 1911
    print '=' * 20
    htls.htls().all(name, age, year)
    print '=' * 20
  except KeyboardInterrupt:
    break
print '\nbye ...'
