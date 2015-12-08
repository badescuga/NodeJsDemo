#!/usr/bin/env python

"""
    Call this from /etc/rc.local
    Will print IP Address on Unicorn HAT upon booting up
"""

import sys
import os
import time
import signal
import datetime
import socket
# replace this with absolute path
sys.path.append(os.path.abspath("lib/"))
from UHScroll import *

UH.brightness(0.10)

def sigterm_handler(signal, frame):
    print '\nSIGTERM received. Cleaning up HAT..'
    UH.clear()
    sys.exit(0)

# Cleanup HAT on SIGTERM (CTRL-C)
signal.signal(signal.SIGTERM, sigterm_handler)

def scroll(msg, color):
    unicorn_scroll(msg, color, 200, 0.07)


#show_letter(special_smilie,'yellow',200)
    #colors = 'orange','blue','white','yellow','green','cyan','pink'
    #show_letter(special_hart,color,200)
    #time.sleep(0.17)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        # s.timeout(2)
        s.connect(('10.1.1.1', 0))
        IP = s.getsockname()[0]
    except:
        IP = 'Cannot get IP'
    finally:
        s.close()
    return IP

ipaddr = get_ip()

scroll('SEBULBA READY:', 'green')
print '\n[SEBULBA] IP Address from Python: ', ipaddr
scroll(ipaddr, 'yellow')
