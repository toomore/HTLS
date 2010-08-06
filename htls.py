#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    print '總計 %s' % total
