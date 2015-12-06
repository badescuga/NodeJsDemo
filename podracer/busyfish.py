#!/usr/bin/env python

import itertools
import sys
import time
from termcolor import colored

fish = itertools.cycle([">))'>    "," >))'>   ","  >))'>  ","   >))'> ","    >))'>","    <'((<","   <'((< ","  <'((<  "," <'((<   ","<'((<    "])
color = 'cyan'


while True:
    sys.stdout.write(colored(fish.next(), color)) # write the next character
    sys.stdout.flush()      # flush stdout buffer (actual character display)
    time.sleep(0.3)
    sys.stdout.write('\r')  # erase the last written char
