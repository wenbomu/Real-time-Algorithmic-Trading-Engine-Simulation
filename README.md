# Real-time-Algorithmic-Trading-Engine-Simulation
In this project, we used socket programming to simulate the SUB-PUB pattern

TickServer.py:
Initialize the socket programming. This file plays the server role in this project. It sends the price of something every second. To simulate the change in price, we used the Monte Carlo Simulation.

BarsServer.py:
Another server. It sends several messages every second.

TickClient.py:
The socket tester, which tells us whether the server works well.

RealTimeDataSockets.ipynb:
This file plays the client's role. In this file, I practiced showing the data in the real-time form. Once we start the files, the data will start to appear on the graph. The first graph shows the raw data. The second graph shows the moving average crossover method. In the third graph, I showed three attributes in separate sub-plots. The fourth graph is a little different. It shows the value of eight items at the same time.
