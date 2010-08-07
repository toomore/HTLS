#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

class htls(object):
  """ HTLS """
  def __init__(self):
    """ Read txt file. """
    self.aw = open('./behao2.txt', 'r').read().split('\n')[:-1]

  def s(self, word):
    """ search Stroke """
    total = 0
    for r in word.decode('utf-8'):
      for i in self.aw:
        ii = i.split(' ')
        if r in ii[2].decode('utf-8'):
          total += int(ii[0])
          print '%s %2s %s' % (r.encode('utf-8'), ii[0], ii[1])
    self.total = total
    print '總計 %s' % total

  def ht(self, age):
    """ HT cal. """
    o = ['成熟運','發展運','巔峰運','老化運','病變運','破滅運','谷底運','蘊釀運','吸收運','成長運']
    oo = ['90-126','126-162','162-198','198-234','234-270','270-306','306-342','342-18','18-54','54-90']
    behao = self.total % 10
    t_age = abs(age - behao)
    print '河圖：%s (%s)' % (o[t_age % 10],oo[t_age % 10])

  def ls(self, year = datetime.today().year - 1911):
    """ LS cal. """
    name = self.total % 9
    ll = ['名','財','官','利','交','拜','衰','煞','絕']
    print '洛書：%s' % ll[abs(year - name) % 9]

  def all(self, name, age, year = datetime.today().year - 1911):
    """ All in one. age for ht, year for ls. """
    self.s(name)
    if age:self.ht(age)
    self.ls(year)
