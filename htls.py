#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

class htls(object):
  """ HTLS """
  def __init__(self, word = None):
    """ Do init. """
    ## Read txt file.
    self.aw = open('./behao2.txt', 'r').read().split('\n')[:-1]

    ## set the HTLS vars.
    self.hts = ['成熟運','發展運','巔峰運','老化運','病變運','破滅運','谷底運','蘊釀運','吸收運','成長運']
    self.htss = ['90-126','126-162','162-198','198-234','234-270','270-306','306-342','342-18','18-54','54-90']
    self.lss = ['名','財','官','利','交','拜','衰','煞','絕']

    ## Run.
    if word: self.s(word)

  def s(self, word):
    """ search Stroke """
    total = 0
    s_op = ''
    for r in word.decode('utf-8'):
      for i in self.aw:
        ii = i.split(' ')
        if r in ii[2].decode('utf-8'):
          total += int(ii[0])
          s_op += '%s %2s %s\n' % (r.encode('utf-8'), ii[0], ii[1])
    self.total = total
    self.s_op = s_op

  def ht(self, age):
    """ HT cal. """
    o = self.hts ## ['成熟運','發展運','巔峰運','老化運','病變運','破滅運','谷底運','蘊釀運','吸收運','成長運']
    oo = self.htss ## ['90-126','126-162','162-198','198-234','234-270','270-306','306-342','342-18','18-54','54-90']
    behao = self.total % 10
    if age < 10: age += 10
    t_age = abs(age - behao)
    return '%s (%s)' % (o[t_age % 10],oo[t_age % 10])

  def ls(self, year = datetime.today().year - 1911):
    """ LS cal. """
    name = self.total % 9
    ll = self.lss ## ['名','財','官','利','交','拜','衰','煞','絕']
    if year < 9: year += 9
    return '%s' % ll[abs(year - name) % 9]

  def all(self, age, year = datetime.today().year - 1911):
    """ All in one. age for ht, year for ls. """
    re = self.s_op + '總計 ' + str(self.total) + '\n'
    if age:re += '河圖：' + self.ht(int(age)) + '\n'
    re += '洛書：' + self.ls(int(year))
    return re

def masscal(q):
  """ mass cal. q must be dict. """
  re = ['name	age year 筆劃 河圖 角度 洛書']
  for i in q:
    try:
      if i:
        name, age, year = i.replace('\t', ' ').split(' ')
        cal = htls(name.encode('utf-8'))
        re.append('%s %s %s %s %s %s %s' % (name.encode('utf-8'), str(age), str(year), str(cal.total), str(cal.ht(int(age))), str(cal.ls(int(year))), str(cal.s_op.replace('\n', ' '))))
      else:
        re.append('')
    except:
      re.append('Format Fault.')
  return re
