
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val 
        self.left = left
        self.right = right

def invertTree(root):
    if not root:
        return None
    

    queue = [root]

    while queue:
        current_node = queue.pop(0)
        print("as",current_node.left)

        current_node.left,current_node.right = current_node.right,current_node.left
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return root
    

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

inverted_root = invertTree(root)

# Print the inverted tree using a breadth-first traversal
queue = [inverted_root]
while queue:
    current_node = queue.pop(0)
    print(current_node.val, end=" ")
    if current_node.left:
        queue.append(current_node.left)
    if current_node.right:
        queue.append(current_node.right)
