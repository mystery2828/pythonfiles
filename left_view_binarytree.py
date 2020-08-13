
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def helper(root,level):
    global max_level
    if not root:
        return
    if max_level<level:
        print(root.data, end=' ')
        max_level=level
    helper(root.left,level+1)
    helper(root.right,level+1)



def LeftView(root):
    '''
    :param root: root of given tree.
    :return: print the left view of tree, dont print new line
    '''
    # code here
    global max_level
    max_level = 0
    level = 1
    return helper(root,level)
