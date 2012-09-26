import threading
from time import sleep
from sys import argv

values = argv[1:]

class thisThread(threading.Thread):

     def run(self):

          n = int(values[x])
          sleep(n)
          print n

for x in range(len(values)):
     thisThread().start()
