#https://pypi.python.org/pypi/socketIO-client
#if script called without args, it goes to production
#if it's called with 'dev' arg, it defaults to localhost

import logging
import sys

#logging.getLogger('requests').setLevel(logging.WARNING)
#logging.basicConfig(level=logging.DEBUG)

from socketIO_client import SocketIO, LoggingNamespace

#defining methods
##################################
def start(*args):
	print('>>> raspberry >>> CONNECTED')
	socketIO.emit('login', { 'connectedType': 'robot','name': 'RaspberryCarRobot'}, callback_login_emit)
	
def on_move_robot(*args):
    print('>>> raspberry >>> on move robot', args)
	
def callback_login_emit(*args):
	print('>>> raspberry >>> callback login emit', args)
	
#executing code
###################################

if len(sys.argv) > 0 and sys.argv[1] == 'dev':
	print('>>> raspberry >>> CONNECTING TO LOCALHOST')
	socketIO = SocketIO('localhost', 3000, LoggingNamespace)
else:
	print('>>> raspberry >>> CONNECTING TO PRODUCTION')
	socketIO = SocketIO('decemberdemoapp.azurewebsites.net', 80, LoggingNamespace)

socketIO.on('moveRobot',on_move_robot)

#generic scenario handled 
socketIO.on('connect', start)
socketIO.on('reconnect', start);

#keep loop opened (i.e. keep socket opened)
socketIO.wait()