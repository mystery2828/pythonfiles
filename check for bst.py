INT_MAX = 4294967296
INT_MIN = -4294967296
  
# A binary tree node 
class newNode: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

def helper(node,mini,maxi):
    if node is None:
        return True
    
    if node.data<mini or node.data>maxi:
        return False
    
    return (helper(node.left,mini,node.data-1) and helper(node.right,node.data+1,maxi))

def check(root):
    return helper(root,INT_MIN, INT_MAX)


root = newNode(4)  
root.left = newNode(2)  
root.right = newNode(5)  
root.left.left = newNode(1)  
root.left.right = newNode(3)  
print(check(root))
