#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twseno import twseno
from htls import htls

allstock = twseno().allstock
n = htls()
for i in allstock:
  print i,allstock[i]
  n.all(allstock[i])
  print '='*15
