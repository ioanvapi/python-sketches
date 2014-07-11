#!/usr/bin/python
# Both two messages will be displayed every 5 seconds, endless,
# but can interchange because the interval is not guarantied.

import threading

def hello(message):
   print(message)
   t = threading.Timer(5.0, hello, [message])
   t.start() # after 5 seconds, message will be printed


hello("Hello world !!!")
hello("Hello mfs !!!\n")

