from collections import deque
import time
import threading

class OrderServe:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def order(self,list):
        for i in list:
            self.enqueue(i)
            print("Request Order : ",i)
            time.sleep(0.5)

    def serve(self):
        while not self.is_empty():
            meal = self.dequeue()
            print("Order Served : ",meal)
            time.sleep(2)

    def print(self):
        print(self.buffer)
 

orders = ['pizza','samosa','pasta','biryani','burger']
os = OrderServe()
#os.order(orders)
#os.serve()


order_thread = threading.Thread(target = os.order,args=(orders,))
serve_thread = threading.Thread(target= os.serve,args=())

order_thread.start()
time.sleep(1)
serve_thread.start()

order_thread.join()
serve_thread.join()


