# Pushover for Weechat

Send private messages and highlights to your iOS/Android device or browser via the Pushover service (https://pushover.net/)

Taken entirely from https://github.com/jamtur01/pushover-weechat but rewritten in Python as the Ruby version stopped being able to load and this was easier than debugging rubygems.

# Install

Load the pushover-weechat.py plugin into Weechat. Place it in the
~/.weechat/python directory:

    /python load pushover-weechat.py

It also requires a Pushover account and Python.

# Requirements

[requests](http://docs.python-requests.org/en/latest/user/install/#install) Python requests library.

### Any recent Python
```
% pip install requests
```

### Debian
```
% apt-get install python-requests
```

# Setup

Set your Pushover user key.

    /set plugins.var.python.pushover-weechat.userkey 123456789abcdefgh

I have an apikey too, as I have more than one application listed in pushover.

    /set plugins.var.python.pushover-weechat.apikey retjatLorpaffucBi

# Options

* plugins.var.python.pushover-weechat.userkey

  The user key for your Pushover service. Defaults to an empty string and must be set for pushover-weechat to work.

* plugins.var.python.pushover-weechat.sound

  Set your notification sound options (Current listing located at https://pushover.net/apisounds)

  Default: blank (Sound will be device default tone set in Pushover)

* plugins.var.python.pushover-weechat.away

  Whether you want to get notifications based on whether you're away or all the time.

  Default: off (will alert all the time, regardless of away status)

# Author

Ben Hughes (<thegithubs@mumble.org.uk>).

With thanks to the original author James Turnbull (<james@lovedthanlost.net>).

# License

MIT

