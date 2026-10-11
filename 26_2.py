# ct25
class Node:
    def __init__(self, value):
        self.value = value
        self.has_x = (value == 'x')  # has x or no
        self.left = None
        self.right = None

def free_tree(node):
    # deletes tied nodes
    if node is None:
        return
    free_tree(node.left)
    free_tree(node.right)
    node.left = None
    node.right = None
    del node

def get_priority(op):
    # * / % are first
    if op == '+' or op == '-': return 1
    if op == '*' or op == '/' or op == '%': return 2
    if op == '^': return 3
    return 0

def calculate(op, a, b):
    # calculates
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a // b
    if op == '%': return a % b
    if op == '^': return int(a ** b)
    return 0

def is_digit(s):
    # if line is a number
    if not s: return False
    if s[0] == '-' and len(s) > 1:
        return s[1:].isdigit()
    return s.isdigit()

def tokenize(expr):
    # split to ops nums x
    tokens = []
    i = 0
    n = len(expr)
    while i < n:
        # no spaces
        if expr[i] in ' \t\n\r':
            i += 1
            continue
        if expr[i] == 'x':
            tokens.append('x')
            i += 1
        elif expr[i].isdigit():
            num = ""
            while i < n and expr[i].isdigit():
                num += expr[i]
                i += 1
            tokens.append(num)
        else:
            tokens.append(expr[i])
            i += 1
    return tokens

def build_tree(tokens):
    # build
    nodes = []
    ops = []

    def process_op():
        if len(nodes) < 2 or not ops:
            return
        op = ops.pop()
        right = nodes.pop()
        left = nodes.pop()
        
        parent = Node(op)
        parent.left = left
        parent.right = right
        parent.has_x = left.has_x or right.has_x
        nodes.append(parent)

    for token in tokens:
        if token == '(': # skobki vonychie
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                process_op()
            if ops:
                ops.pop()  # del (
        elif token in ('+', '-', '*', '/', '%', '^'):
            # >= stricly l to r
            while ops and get_priority(ops[-1]) >= get_priority(token):
                process_op()
            ops.append(token)
        else:
            nodes.append(Node(token))

    while ops:
        process_op()

    return nodes[0] if nodes else None

def evaluate(root, x_val):
    # solve
    if root is None:
        return 0
    if root.value == 'x':
        return x_val
    if is_digit(root.value):
        return int(root.value)

    left_val = evaluate(root.left, x_val)
    right_val = evaluate(root.right, x_val)
    return calculate(root.value, left_val, right_val)

def transform_tree(root):
    # transforms where no x
    if root is None:
        return None

    # neighbors
    root.left = transform_tree(root.left)
    root.right = transform_tree(root.right)

    # there transform
    if not root.has_x and (root.left or root.right):
        val = evaluate(root, 0)
        
        # del lr
        free_tree(root.left)
        free_tree(root.right)
        
        root.left = None
        root.right = None
        root.value = str(val)  # replace

    return root

def print_tree_sideways(root, file, level=0):
    # print tree blin
    if root is None:
        return

    # inorder
    print_tree_sideways(root.right, file, level + 1)

    # spaces
    # current 8 * (level + 1)
    target_width = 8 * (level + 1)
    val_len = len(root.value)
    spaces_needed = target_width - val_len
    
    # file
    file.write(" " * spaces_needed + root.value + "\n")

    print_tree_sideways(root.left, file, level + 1)

def main():
    # launch
    x_value = int(input("Input x: "))

    # read
    try:
        with open("FN1.txt", "r") as f:
            expression = f.read()
    except FileNotFoundError:
        print("FN1 not exists.")
        return

    # strip
    expression = expression.strip() if hasattr(expression, 'strip') else expression

    tokens = tokenize(expression)
    root = build_tree(tokens)

    if not root:
        print("Error while building.")
        return

    # solve eq
    final_result = evaluate(root, x_value)

    # free
    root = transform_tree(root)

    # fn2
    with open("FN2.txt", "w") as f:
        f.write("Result with x = " + str(x_value) + ": " + str(final_result) + "\n\n")
        f.write("Tree:\n")
        print_tree_sideways(root, f)

    print("FN2 rewritten.")

if __name__ == "__main__":
    main()
