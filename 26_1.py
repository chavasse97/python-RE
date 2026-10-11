# ct7
import os

# Класс узла бинарного дерева
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# replace dict
OP_MAP = {'+': -1, '-': -2, '*': -3, '/': -4, '%': -5, '^': -6}

def calc(op_code, a, b):
    # coded op
    if op_code == -1: return a + b
    if op_code == -2: return a - b
    if op_code == -3: return a * b
    if op_code == -4: return a // b
    if op_code == -5: return a % b
    if op_code == -6: return a ** b
    raise ValueError("Wrong operation")

def build_tree(tokens):
    # tree
    if not tokens:
        return None
    
    token = tokens.pop(0)
    
    # tokrn is op
    if token in OP_MAP:
        node = Node(OP_MAP[token])
        node.left = build_tree(tokens)
        node.right = build_tree(tokens)
        return node
    # token is num
    else:
        return Node(int(token))

def transform_tree(node):
    # 0 9
    if node is None:
        return None

    # rec lr
    node.left = transform_tree(node.left)
    node.right = transform_tree(node.right)

    # if current is op and lr are num
    if node.value < 0 and node.left and node.right:
        if node.left.value >= 0 and node.right.value >= 0:
            try:
                res = calc(node.value, node.left.value, node.right.value)
                # if 0 9 delete nodes
                if 0 <= res <= 9:
                    node.value = res
                    node.left = None
                    node.right = None
            except ZeroDivisionError:
                # exception
                pass

    return node

def solve(filename):
    # fileread
    with open(filename, 'r') as f:
        expression = f.read().strip()
    
    # splitter
    tokens = expression.split()
    
    root = build_tree(tokens)
    
    root = transform_tree(root)
    
    return root

# launch
root_ptr = solve('calctree7.txt')
print(f"Root ptr: {root_ptr}, Root value: {root_ptr.value if root_ptr else None}")
