# tree10
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BirdTreeCameraAnalyser:
    def __init__(self):
        self.cameras = 0
        # camera set
        self.camera_nodes = set()
        # how much cameras checks node
        self.coverage_count = {}

    def analyse_coverage(self, root):
        # checks nodes with 2+ cams
        if not root:
            return 0
        
        self.cameras = 0
        self.camera_nodes.clear()
        self.coverage_count.clear()

        # postorder
        # 0 - no cam
        # 1 - no cam but seen
        # 2 - cam
        def dfs_placement(node):
            if not node:
                return 1 # empty = checked

            left_status = dfs_placement(node.left)
            right_status = dfs_placement(node.right)

            # no l/r cam = cam root
            if left_status == 0 or right_status == 0:
                self.camera_nodes.add(node)
                return 2

            # l/r cam = root cammed
            if left_status == 2 or right_status == 2:
                return 1

            # no cam else
            return 0

        # root
        if dfs_placement(root) == 0:
            self.camera_nodes.add(root)

        # intersect
        # inc count
        def add_coverage(node):
            if node:
                self.coverage_count[node] = self.coverage_count.get(node, 0) + 1

        # post again for overlap
        def calculate_overlaps(node, parent=None):
            if not node:
                return

            # cam coverage
            if node in self.camera_nodes:
                add_coverage(node)
                add_coverage(parent)
                add_coverage(node.left)
                add_coverage(node.right)

            calculate_overlaps(node.left, node)
            calculate_overlaps(node.right, node)

        calculate_overlaps(root)

        # overcover
        overcovered_nodes = sum(1 for node, count in self.coverage_count.items() if count > 1)
        
        return overcovered_nodes

# test

def insert_balanced(arr, root, i, n):
    if i < n and arr[i] is not None:
        temp = Node(arr[i])
        root = temp
        root.left = insert_balanced(arr, root.left, 2 * i + 1, n)
        root.right = insert_balanced(arr, root.right, 2 * i + 2, n)
    return root

if __name__ == "__main__":
    #          1
    #        /   \
    #       2<    3<
    #      / \   /
    #     4<  5 6
    #    /
    #   7
    
    tree_elements = [1, 2, 3, 4, 5, 6, None, 7]
    root = insert_balanced(tree_elements, None, 0, len(tree_elements))

    analyser = BirdTreeCameraAnalyser()
    result = analyser.analyse_coverage(root)
    
    print(f"Minimum amount of cams: {len(analyser.camera_nodes)}")
    print(f"Nodes with cam: {[node.key for node in analyser.camera_nodes]}")
    print(f"Overcovered nodes amount: {result}")
