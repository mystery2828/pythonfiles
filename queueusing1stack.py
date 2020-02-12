import time
start = time.time()

class Queue1Stack(object):
    
    def __init__(self):
        self.stack = []
    def enqueue(self,item):
        self.stack.append(item)
        
    def dequeue(self):
        return self.stack.pop(0)
q = Queue1Stack()

for i in range(5000):
    q.enqueue(i)


for i in range(5000):
    print(q.dequeue())

print(time.time()-start)