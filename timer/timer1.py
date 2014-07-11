#!/usr/bin/python
# 'Hello world !!!' message will be displayed every 5 seconds, endless

import threading


def hello():
    print("Hello world !!!")
    t = threading.Timer(5.0, hello)
    t.start()  # after 5 seconds, "hello, world" will be printed


hello()

