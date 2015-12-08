#https://pypi.python.org/pypi/socketIO-client
#if script called without args, it goes to production
#if it's called with 'dev' arg, it defaults to localhost

from sebulba import *
import logging
import sys
import requests
import time
from threading import Thread
import requests

#sys.setdefaultencoding('utf-8')

#logging.getLogger('requests').setLevel(logging.WARNING)
#logging.basicConfig(level=logging.DEBUG)

from socketIO_client import SocketIO, LoggingNamespace

#defining methods
##################################
def start(*args):
	print('>>> raspberry >>> CONNECTED')
	socketIO.emit('login', { 'connectedType': 'robot','name': 'RaspberryCarRobot'}, callback_login_emit)
	
def on_disconnect(*args):
	print('>>> raspberry >>> disconnected from server')
	
def on_move_robot(*args):
    print('>>> raspberry >>> on move robot', args)
	
def callback_login_emit(*args):
	print('>>> raspberry >>> callback login emit', args)
	
#executing code
###################################

if len(sys.argv) > 1 and sys.argv[1] == 'dev':
	print('>>> raspberry >>> CONNECTING TO LOCALHOST')
	socketIO = SocketIO('localhost', 3000, LoggingNamespace)
else:
	print('>>> raspberry >>> CONNECTING TO PRODUCTION')
	socketIO = SocketIO('decemberdemoapp.azurewebsites.net', 80, LoggingNamespace)

socketIO.on('moveRobot',on_move_robot)

#generic scenario handled 
socketIO.on('connect', start)
socketIO.on('reconnect', start);
socketIO.on('disconnect', on_disconnect);

def sendStream():
	print('starting sending stream')
	while 1:
       		r = requests.get('http://localhost:8080/?action=stream/',stream=True)
		#print('sending stream data '+r.ra
		for chunk in r.iter_content(decode_unicode=True):
			val = chunk
        		print('sending.. '+val)
			socketIO.emit('receivedImageStreamFromPi',val)
		time.sleep(1)

t = Thread(target=sendStream)
t.daemon = True
t.start()

#keep loop opened (i.e. keep socket opened)
socketIO.wait()
#socketIO.wait(seconds=1)

