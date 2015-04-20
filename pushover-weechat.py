#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# -----------------------------------------------------------
# Filename      : pushover-weechat.py
# Description   : copied from https://github.com/jamtur01/pushover-weechat
# Created By    : Ben Hughes
# Date Created  : 2015-04-19 13:37
#
# License       : MIT
#
# (c) Copyright 2015, Etsy all rights reserved.
# -----------------------------------------------------------
__author__ = "Ben Hughes"
__version__ = "0.1"

import re
import requests
import weechat as w

SCRIPT_NAME = 'pushover-weechat'
SCRIPT_AUTHOR = __author__
SCRIPT_DESC = 'Send highlights and private messages in channels to your phone'
SCRIPT_VERSION = __version__
SCRIPT_LICENSE = 'MIT'

DEFAULTS = {
    'apikey': 'eWEPQ0QQrM2A4WBfx8zZoEpYWBAuBa',
    'userkey': '',
    'sound': '',
    'away': 'off'
    # 'interval': '60',
}


def donotification(data, signal, signal_data):

    if w.config_get_plugin('away') == 'on':
        buffer = w.current_buffer()
        if w.buffer_get_string(buffer, "localvar_away") == "":
            return w.WEECHAT_RC_OK

    from_nick, message = re.split('\s', signal_data, 1)

    if signal == 'weechat_pv':
        event = 'Weechat Private message from ' + from_nick
    elif signal == 'weechat_highlight':
        event = 'Weechat Highlight from ' + from_nick

    if notify(w.config_get_plugin('apikey'),
              w.config_get_plugin('userkey'),
              event,
              message):
        return w.WEECHAT_RC_OK
    else:
        return w.WEECHAT_RC_ERROR


def notify(token, user, title, message, sound=None):

    apiurl = 'https://api.pushover.net/1/messages'
    payload = {'token': token, 'user': user,
               'title': title, 'message': message}
    if sound is not None and sound != '':
        payload['sound'] = sound

    r = requests.post(apiurl, params=payload, verify=True)
    return r.status_code == requests.codes.ok

if w.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE,
              SCRIPT_DESC, '', ''):
    for option, default_value in DEFAULTS.iteritems():
        if not w.config_is_set_plugin(option):
            w.config_set_plugin(option, default_value)

    w.prnt('', 'pushover-weechat: Please set your API key with:'
               ' /set plugins.var.python.pushover-weechat.userkey')

    w.hook_signal('weechat_highlight', 'donotification', '')
    w.hook_signal('weechat_pv', 'donotification', '')
