# tree6
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findmax(root: TreeNode) -> int:
    # empty
    if root is None:
        raise ValueError("Tree is empty")
        
    current = root
    while current.right is not None:
        current = current.right
        
    return current.value

#        10
#       /  \
#      5    15
#     / \     \
#    3   7     18

P1 = TreeNode(10)
P1.left = TreeNode(5, TreeNode(3), TreeNode(7))
P1.right = TreeNode(15, None, TreeNode(18))

# launch
max_value = findmax(P1)
print(f"Max: {max_value}")  # 18
