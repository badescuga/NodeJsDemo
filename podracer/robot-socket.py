#https://pypi.python.org/pypi/socketIO-client
#if script called without args, it goes to production
#if it's called with 'dev' arg, it defaults to localhost

# Import servo logic from sebulba.py
from sebulba import *

import logging
import sys
import requests
import time
from threading import Thread
import requests
import base64

reload(sys)
sys.setdefaultencoding('cp437')

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
    direction = args[0]['direction']
    print 'RECEIVED', direction
    if direction == 'up':
        print 'DRIVING', direction
        racer_move('FORWARD', 1)
    if direction == 'down':
        print 'DRIVING', direction
        racer_move('BACKWARD', 1)
    if direction == 'left':
        print 'DRIVING', direction
        racer_turn('LEFT', 1)
    if direction == 'right':
        print 'DRIVING', direction
        racer_turn('RIGHT', 1)

def callback_login_emit(*args):
	print('>>> raspberry >>> callback login emit; starting video stream', args)
	t = Thread(target=sendStream)
	t.daemon = True
	t.start()

	
def sendStream():
	print('starting sending stream')
	while 1:
	    	r = requests.get('http://localhost:8080/?action=snapshot/',stream=True)
		val = r.raw.data
		#for line in r.iter_lines():
		#	val = val + line
		val = base64.b64encode(val)
	#	print(' -- '+val)
	#	print(type(val))
		socketIO.emit('receivedImageStreamFromPi',val)
		#time.sleep(.05)
	#break


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

#keep loop opened (i.e. keep socket opened)
socketIO.wait()
#socketIO.wait(seconds=1)

