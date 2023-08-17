import zmq
import math
import time
import random

context  =zmq.Context()
# context api, can find the protocol, then we can create a server
socket = context.socket(zmq.PUB)
# connect socket to local IP address (conputer, 0.0.0.0), local host
socket.bind('tcp://0.0.0.0:5555')
# 端口是5555, from 0 to 65???, we need local host and address

class InstrumentPrice(object):
    def __init__(self):
        self.symbol = 'SYMBOL'
        self.t = time.time()
        self.value = 100.
        # imply this is a float
        self.r = 0.01
        self.sigma = 0.4
    
    def simulate_value(self):
        # when this func is invoked, the current time is recorded
        t=time.time()
        # denomator is the work seconds per year
        dt = (t - self.t) / (252 * 8 * 60 * 60)
        # make dt larger to amplify its change
        dt *= 500
        # update the value of t
        self.t = t

        self.value *= math.exp((self.r - 0.5 * self.sigma ** 2) * dt + \
            self.sigma * math.sqrt(dt) * random.gauss(0, 1))
        
        return self.value

ip = InstrumentPrice()

while True:
    msg = '{} {:.2f}'.format(ip.symbol, ip.simulate_value())
    print(msg)
    socket.send_string(msg)
    time.sleep(random.random()*2)


