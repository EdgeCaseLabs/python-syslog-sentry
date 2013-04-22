# Sentry Syslog Forwarder

This is a simple [Sentry](https://github.com/getsentry) raven client wrapper to receive Syslog events and send them to your Sentry server.

I'm using this currently for some devices on my network that can send out Syslog events that I wish to be routed to Sentry instead.


Based on [https://github.com/iobear/beewatch/blob/master/bin/psyslog.py](https://github.com/iobear/beewatch/blob/master/bin/psyslog.py)


## Installation

	$ pip install raven
	
## Configuration

1. Edit `SENTRY_DSN` in `psyslog.py` to point to your Sentry server.
2. Edit `HOST` for your IP address where installed.
	
## Tests

In one console, run the syslog server:

	$ sudo python psyslog.py 

In another console, run the tests:

	$ python -m unittest tests


Note: You may see `No handlers could be found for logger "sentry.errors"` in the Syslog console. You can ignore this.

