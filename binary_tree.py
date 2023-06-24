class Node:
    def __init__(self,item,left=None,right=None):
        self.left = left
        self.right = right
        self.val = item

def inorder(root):
    if not root:
        return []
    
    return inorder(root.left)+[root.val]+inorder(root.right)

def preorder(root):
    if not root:
        return []
    
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):
    if not root:
        return []
    
    return postorder(root.left) + postorder(root.right) + [root.val]


root = Node(0)

root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)


inorder_traverse = inorder(root)
print("inorder",inorder_traverse)
preorder_traverse = preorder(root)
print("preorder",preorder_traverse)
postorder_traverse = postorder(root)
print("postorder",postorder_traverse)