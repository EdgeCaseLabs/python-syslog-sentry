import logging
import logging.handlers

import unittest

class TestSysLogHandler(unittest.TestCase):

	def setUp(self):
		pass

	def test_sys_log(self):

		my_logger = logging.getLogger("sentry.errors")
		my_logger.setLevel(logging.DEBUG)

		handler = logging.handlers.SysLogHandler(address = ('0.0.0.0',514))

		my_logger.addHandler(handler)

		my_logger.debug('this is debug')
		my_logger.critical('this is critical')


if __name__ == '__main__':
    unittest.main()