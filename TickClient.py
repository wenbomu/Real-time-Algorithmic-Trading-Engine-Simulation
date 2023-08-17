import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://0.0.0.0:5555')

socket.setsockopt_string(zmq.SUBSCRIBE, 'SYMBOL')

while True:
    data = socket.recv_string()
    print(data)

# the way to run
# open two terminal, two bash
# input command line "python3 tickserver.py" and ...
# in two window
