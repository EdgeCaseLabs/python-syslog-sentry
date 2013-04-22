#!/usr/bin/python

SENTRY_DSN = '<SENTRY DSN>'
HOST = "0.0.0.0"
PORT = 514

import SocketServer
import time
from raven import Client

client = Client(SENTRY_DSN)

class SyslogUDPHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		global client
		data = bytes.decode(self.request[0].strip())

		laengde = len(data)
		if laengde > 4:
			newLogString = "%s %s %s\n" % (int(time.time()), self.client_address[0], data)
			
			client.captureMessage(newLogString)



if __name__ == "__main__":
	try:
		server = SocketServer.UDPServer((HOST, PORT), SyslogUDPHandler)
		server.serve_forever()
	except (IOError, SystemExit):
		raise
	except KeyboardInterrupt:
		print ("Crtl+C Pressed. Shutting down.")