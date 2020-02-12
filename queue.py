class Queue(object):
    def __init__(self):
        self.items = []
        self.next = None
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

