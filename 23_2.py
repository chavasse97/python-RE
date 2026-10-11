# tree10
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert(root: TreeNode, x: int) -> TreeNode:
    new_node = TreeNode(x)
    
    if root is None:
        return new_node
        
    current = root
    while True:
        if x < current.value:
            if current.left is None:
                current.left = new_node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = new_node
                break
            current = current.right
            
    return root

#        10
#       /  \
#      5    15

P1 = TreeNode(10)
P1.left = TreeNode(5)
P1.right = TreeNode(15)

# launch
X = 8
P1 = insert(P1, X)

print("Done")
print(P1.left.right.value)
