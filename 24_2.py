# tree5
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class PostOrderIterator:
    def __init__(self, root):
        self.stack = []
        if root:
            # root, isvisited
            self.stack.append((root, False))

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration

        while self.stack:
            curr, right_visited = self.stack.pop()

            # return if checked
            if right_visited:
                return curr.key

            # LR if 1st visit
            self.stack.append((curr, True))

            if curr.right:
                self.stack.append((curr.right, False))
            if curr.left:
                self.stack.append((curr.left, False))


# insert
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

if __name__ == "__main__":
    #        4
    #       / \
    #      2   5
    #     / \
    #    1   3
    root = None
    keys = [4, 2, 5, 1, 3]
    for key in keys:
        root = insert(root, key)

    print("Postorder:")
    iterator = PostOrderIterator(root)
    
    # launch
    for val in iterator:
        print(val, end=" ")
    print()
