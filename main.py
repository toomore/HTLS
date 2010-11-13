#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2010 Toomore Chiang, http://toomore.net/
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from google.appengine.ext import webapp
from google.appengine.api import xmpp
from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp.util import login_required
from google.appengine.ext.webapp import template

#from google.appengine.api import urlfetch
import logging,htls

############## webapp Models ##############
class MainPage(webapp.RequestHandler):
  def get(self):
    self.response.out.write(template.render('./template/hh_index.htm',{}))

############## webapp Models ###################
class xmpp_invite(webapp.RequestHandler):
  @login_required
  def get(self):
    umail = users.get_current_user().email()
    xmpp.send_invite(umail)
    xmpp.send_message('toomore0929@gmail.com', '#NEWUSER %s' % umail)
    logging.info('#NEWUSER %s' % umail)
    ## todo: send a guild mail to the first time invited user.
    tv = {'umail': umail}
    self.response.out.write(template.render('./template/hh_invite.htm',{'tv': tv}))
    #self.redirect('http://www.gmail.com/')

class xmpp_pagex(webapp.RequestHandler):
  def post(self):
    msg = xmpp.Message(self.request.POST)
    if 'help' in msg.body:
      msg.reply('\r\n<姓名> <年齡> <計算流年（民國年）>')
    elif 'ht' in msg.body:
      hts = htls.htls().hts
      re = ''
      for i in hts:
        re += i + '→'
      msg.reply(re)
    elif 'ls' in msg.body:
      lss = htls.htls().lss
      re = ''
      for i in lss:
        re += i + '→'
      msg.reply(re)
    else:
      try:
        st = msg.body.split(' ')
        re = htls.htls(st[0].encode('utf-8')).all(st[1],st[2])
        msg.reply('\r\n' + re)
        logging.info('HTLS: %s' % re)
      except:
        msg.reply('輸入錯誤！請參考說明文件：https://github.com/toomore/HTLS/wiki/GTalk')
    #msg.reply(msg.body)
    logging.info(self.request.POST)
    logging.info('Msg status: %s' % msg.body)

############## main Models ##############
def main():
  """ Start up. """
  application = webapp.WSGIApplication(
                                      [
                                        ('/', MainPage),
                                        ('/chat/', xmpp_invite),
                                        ('/_ah/xmpp/message/chat/', xmpp_pagex)
                                      ],debug=True)
  run_wsgi_app(application)

if __name__ == '__main__':
  main()
