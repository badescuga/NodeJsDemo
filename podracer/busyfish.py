#!/usr/bin/env python

import itertools
import sys
import time
from termcolor import colored

spinner = itertools.cycle([">))'>    "," >))'>   ","  >))'>  ","   >))'> ","    >))'>","    <'((<","   <'((< ","  <'((<  "," <'((<   ","<'((<    "])
color = 'cyan'


while True:
    sys.stdout.write(colored(spinner.next(), color)) # write the next character
    sys.stdout.flush()      # flush stdout buffer (actual character display)
    time.sleep(0.3)
    sys.stdout.write('\r')  # erase the last written char
