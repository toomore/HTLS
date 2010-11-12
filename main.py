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

#from google.appengine.api import urlfetch
import logging,htls

############## webapp Models ##############
class MainPage(webapp.RequestHandler):
  def get(self):
    msg = """
HTLS 和圖洛書 <a href="/chat/">索取邀請函</a>
"""
    self.response.out.write(msg)

############## webapp Models ###################
class xmpp_invite(webapp.RequestHandler):
  @login_required
  def get(self):
    umail = users.get_current_user().email()
    xmpp.send_invite(umail)
    ## todo: send a guild mail to the first time invited user.
    self.response.out.write('%s invited. Please check out your <a href="http://www.gmail.com/">GTalk</a>.' % umail)
    #self.redirect('http://www.gmail.com/')

class xmpp_pagex(webapp.RequestHandler):
  def post(self):
    msg = xmpp.Message(self.request.POST)
    if 'help' in msg.body:
      msg.reply('\r\n<姓名> <年齡> <計算流年（民國年）>')
    else:
      st = msg.body.split(' ')
      re = htls.htls(st[0].encode('utf-8')).all(st[1],st[2])
      msg.reply('\r\n' + re)
      logging.info('HTLS: %s' % re)
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
