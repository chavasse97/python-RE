# tree19
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def isbalanced(root: TreeNode) -> bool:
    
    # returns cortage: (is_balanced, total_nodes)
    def check_balance(node: TreeNode) -> tuple[bool, int]:
        # empty
        if node is None:
            return True, 0
        
        # left
        left_balanced, left_count = check_balance(node.left)
        if not left_balanced:
            return False, 0
            
        # right
        right_balanced, right_count = check_balance(node.right)
        if not right_balanced:
            return False, 0
            
        # current
        # check RL
        current_balanced = abs(left_count - right_count) <= 1
        
        total_nodes = left_count + right_count + 1
        
        return current_balanced, total_nodes

    # launch
    balanced, _ = check_balance(root)
    return balanced

P1 = TreeNode(1)
P1.left = TreeNode(2, TreeNode(4), None)
P1.right = TreeNode(3)

print(isbalanced(P1))  # True

P2 = TreeNode(1)
P2.left = TreeNode(2, TreeNode(4), TreeNode(5))
P2.right = TreeNode(3)

print(isbalanced(P2))  # False
