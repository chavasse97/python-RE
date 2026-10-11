# tw67
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    # insert
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def get_height(node):
    # h
    if node is None:
        return 0
    return 1 + max(get_height(node.left), get_height(node.right))

def get_balance(node):
    # balance
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)

def rotate_right(y):
    # RR
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    return x

def rotate_left(x):
    # LL
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    return y

def rl_rotation_auto(root):
    # rec check balance and RLs
    if root is None:
        return None

    # checker
    root.left = rl_rotation_auto(root.left)
    root.right = rl_rotation_auto(root.right)

    balance = get_balance(root)

    # right unbalanced
    if balance == -2 and root.right:
        right_balance = get_balance(root.right)
        
        # right has left unbalanced = RL
        if right_balance > 0:
            # RR R
            root.right = rotate_right(root.right)
            # LL curr
            return rotate_left(root)

    return root

def main():
    filename = "avl67.txt"  # file
    
    try:
        with open(filename, "r") as f:
            line = f.readline()
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return

    # splitter
    numbers = [int(x) for x in line.split()]
    if not numbers:
        print("Empty file.")
        return

    # BST
    root = None
    for num in numbers:
        root = insert(root, num)

    # avlling
    root = rl_rotation_auto(root)
    print("Balancing done.")

    # root
    if root:
        print(f"Root: {root.value}")
    else:
        print("Root: tree is empty.")

if __name__ == "__main__":
    main()
