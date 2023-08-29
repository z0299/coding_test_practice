class Node:
    def __init__(self, value = None, lvalue = None, rvalue = None):
        self.value = value
        self.left = lvalue
        self.right = rvalue
        
class Tree:
    def __init__(self, root = None):
        self.root = root
        
    def postOrder(self, node):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.value, end=' ')
            
def recursive(pre_lst, in_lst, root, a):
    i = in_lst.index(root)
    ileft = in_lst[:i]
    iright = in_lst[i+1:]
    pleft = pre_lst[1:len(pre_lst)-len(iright)]
    pright = pre_lst[len(pre_lst)-len(iright):]
    if len(pleft) > 0:
        a.left = Node(pleft[0])
    if len(pright) > 0:
        a.right = Node(pright[0])
    # print(pleft, pright)
    # print(ileft, iright)
    
    if len(pleft) > 1:
        if len(pleft) == 2:
            if pleft[1] == ileft[0]:
                a.left.left = Node(pleft[1])
            else:
                a.left.right = Node(pleft[1])
        else:
            recursive(pleft, ileft, pleft[0], a.left)
    
    if len(pright) > 1:
        if len(pright) == 2:
            if pright[1] == iright[0]:
                a.right.left = Node(pright[1])
            else:
                a.right.right = Node(pright[1])
        else:
            recursive(pright, iright, pright[0], a.right)
    
    return
        
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    
    tree = Tree()
    tree.root = Node(preorder[0])
    recursive(preorder, inorder, preorder[0], tree.root)
    # i = inorder.index(preorder[0])
    # left = inorder[:i]
    # right = inorder[i+1:]
    # recursive(left)
    # print(tree.root.left.value)
    tree.postOrder(tree.root)
    print()