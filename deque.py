class Deque(object):
    def __init__(self):
        self.items = []
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removefront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def getFront(self):
        return self.items[len(self.items)-1]
    def getRear(self):
        return self.items[0]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

d = Deque()
d.addFront('hello')
d.addFront('world')
d.addRear(5)
d.addRear(10)
print(d.size())
print(d.isEmpty())
print(d.getFront())
print(d.getRear())