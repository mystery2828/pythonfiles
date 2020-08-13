from collections import defaultdict

def Inorder(root, hd,height):
    if root is None: # base case
        return

    # call left child with one less horizontal distance and height increases by one
    Inorder(root.left,hd-1,height+1)

    if hd in bottomView.hrz_map: # check if the hd exits in the map
        # check if it has height not less than already exiting node
        if bottomView.hrz_map[hd][0] <= height :
            # update the value
            bottomView.hrz_map[hd] = [height,root.data] # insert the pair of height and value
    else:
        # insert this first timer horizontal distance node in map
        bottomView.hrz_map[hd] = [height,root.data] # insert the pair of height and value

    # call for right child
    Inorder(root.right,hd+1,height+1)


def bottomView(root):
    '''
    :param root: root of the binary tree
    :return: list containing the bottom view from left to right
    '''
    res = []
    if root == None: # base case
        return res

    # map to store key as horizontal distance and value as pair of height and value of node
    bottomView.hrz_map = defaultdict(list)

    # do inorder traversal updating our hrz_map.
    Inorder(root,0,0) # 0,0 is for horizontal and height of root as parameters.

    # now for every corresponding horizontal distance, we have max height element in map
    # traverse the map and sort according to distance, then print it
    list_pair =[] # store hrz dist and value pair
    for hd in bottomView.hrz_map:
        list_pair.append([hd,bottomView.hrz_map[hd][1]])
    list_pair.sort()

    # print the values
    for pair in list_pair:
        res.append(pair[1])

    return res
