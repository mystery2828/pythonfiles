class Queue(object):
    def __init__(self):
        self.items = []
        self.next = None
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[-1]

class Node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self, data, cur_pos):
        if data < cur_pos.data:
            if cur_pos.left == None:
                cur_pos.left = Node(data)
            else:
                self._insert(data, cur_pos.left)
        elif data > cur_pos.data:
            if cur_pos.right == None:
                cur_pos.right = Node(data)
            else:
                self._insert(data, cur_pos.right)
        else:
            print("No duplicate are allowed")
    
    def find(self,data):
        if self.root:
            found = self._find(data, self.root)
            if found:
                return True
            return False
        else:
            return None

    def _find(self, data, cur_pos):
        if data < cur_pos.data and cur_pos.left:
            return self._find(data, cur_pos.left)
        elif data > cur_pos.data and cur_pos.right:
            return self._find(data, cur_pos.right)
        if data == cur_pos.data:
            return True

    def traverse(self, typeoftraversal):
        if typeoftraversal == 'preorder':
            return self.pre_order(self.root,'')
        elif typeoftraversal == 'inorder':
            return self.in_order(self.root,'')
        elif typeoftraversal == 'postorder':
            return self.post_order(self.root, '')
        elif typeoftraversal == 'levelorder':
            return self.levelorder(self.root)

    def pre_order(self, start, traversal):
        if start:
            traversal+= (str(start.data) + '-')
            traversal = self.pre_order(start.left,traversal)
            traversal = self.pre_order(start.right,traversal)
        return traversal

    def in_order(self, start, traversal):
        if start:
            traversal = self.in_order(start.left, traversal)
            traversal+= (str(start.data) + '-')
            traversal = self.in_order(start.right, traversal)
        return traversal

    def post_order(self, start, traversal):
        if start:
            traversal = self.post_order(start.left, traversal)
            traversal = self.post_order(start.right, traversal)
            traversal+=(str(start.data) + '-')
        return traversal

    def levelorder(self, start):
        if start is None:
            return 
        traversal = ''
        queue = Queue()
        queue.enqueue(start)
        while not queue.isEmpty():
            traversal += str(queue.peek().data) + '- '
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

bst = BST()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(4)
bst.insert(9)
bst.insert(12)
# lis = [2,5,6,1,6,1,3,5,5,6,2,5]
# for ele in lis:
#     bst.insert(ele)

print(bst.traverse('levelorder'))