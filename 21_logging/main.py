import logging

# needs to be set for displaying messages for DEBUG level and above
# logging.basicConfig(level=logging.DEBUG)
# print(logging.debug('Looks like rain')); # does not print anything by defult
# print(logging.info('And hail')); # does not print anything
# print(logging.warn('Did I hear thunder?')); # default log level
# print(logging.error('Was that lightning?'));
# print(logging.critical('Stop fencing and get kl'));


# logger object; each logger has a name
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger('bunyan')
# logger.debug('Timber!')


# direct logging to a file; had to comment out the code above as otherwise it
# does not write to file; the loggin handler includes at least 15 handlers to
# send messages to places such as email and web servers as well as screen and
# files
# logging.basicConfig(level='DEBUG', filename='blue_ox.log')
# logger = logging.getLogger('bunyan')
# logger.debug('Where is my axe?')
# logger.warn('I need my axe')

fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level='DEBUG', format=fmt)
logger = logging.getLogger('bunyan')
logger.error("This is an error log message")
