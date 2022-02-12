"""

    Node Module

"""


__all__ = ['Node', 'rotate_left', 'rotate_right']


class Node:
    def __init__(self, data):
        self.data = data
        self.right: Node = None
        self.left: Node = None

    def insert(self, data):
        if self.data == data:
            return

        if data > self.data:
            if self.right is None:
                self.right = Node(data=data)
            else:
                self.right.insert(data=data)
                self.right = self.right.fix_imbalance()

        elif data < self.data:
            if self.left is None:
                self.left = Node(data=data)
            else:
                self.left.insert(data=data)
                self.left = self.left.fix_imbalance()

    def search(self, target):
        if self.data == target:
            return self.data
        elif self.right and self.data > target:
            return self.right.search(target)
        elif self.left and self.data < target:
            return self.left.search(target)
        print("value not in tree")

    def traverse_preorder(self):
        print(self.data)
        if self.left:
            self.left.traverse_preorder()
        if self.right:
            self.right.traverse_preorder()

    def traverse_inorder(self):
        if self.left:
            self.left.traverse_inorder()
        print(self.data)
        if self.right:
            self.right.traverse_inorder()

    def traverse_postorder(self):
        if self.left:
            self.left.traverse_postorder()
        if self.right:
            self.right.traverse_postorder()
        print(self.data)

    def height(self, h=0):
        left_height = self.left.height(h=h+1) if self.left else h
        right_height = self.right.height(h=h+1) if self.right else h
        return max(left_height, right_height)

    def get_node_at_depth(self, depth, nodes: list = []):
        if depth == 0:
            nodes.append(self)
            return nodes
        if self.left:
            self.left.get_node_at_depth(depth=depth-1, nodes=nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        if self.right:
            self.right.get_node_at_depth(depth=depth-1, nodes=nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        return nodes

    def min(self):
        if self.left:
            return self.left.min()
        return self.data

    def max(self):
        if self.right:
            return self.right.max()
        return self.data

    def delete(self, target):
        if self.data == target:
            if self.right and self.left:
                min_val = self.right.min()
                self.data = min_val
                self.right = self.right.delete(target=min_val)
                return self
            else:
                return self.left or self.right

        if target > self.data and self.right:
            self.right = self.right.delete(target=target)
        if target < self.data and self.left:
            self.left = self.left.delete(target=target)
        return self.fix_imbalance()

    def rotate_right(self):
        pivot = self.left
        reattach_node = pivot.right
        self.left = reattach_node
        pivot.right = self
        return pivot

    def rotate_left(self):
        pivot = self.right
        reattach_node = pivot.left
        self.right = reattach_node
        pivot.left = self
        return pivot

    def is_balanced(self):
        left_height = self.left.height() + 1 if self.left else 0
        right_height = self.right.height() + 1 if self.right else 0
        return abs(left_height - right_height) < 2

    def left_right_height_diff(self):
        left_height = self.left.height() + 1 if self.left else 0
        right_height = self.right.height() + 1 if self.right else 0
        return left_height - right_height

    def to_str(self):
        if not self.is_balanced():
            return f"{self.data}*"
        return f"{self.data}"

    def fix_imbalance(self):
        if self.left_right_height_diff() > 1:
            # left imbalance
            if self.left.left_right_height_diff() > 0:
                # left, left imbalance
                return rotate_right(self)
            else:
                # left right imbalance
                self.left = rotate_left(self.left)
                return rotate_right(self)

        elif self.left_right_height_diff() < -1:
            # right imbalance
            if self.right.left_right_height_diff() < 0:
                # right, right imbalance
                return rotate_left(self)
            else:
                # right left imbalance
                self.right = rotate_right(self.right)
                return rotate_left(self)
        return self

    def rebalance(self):
        if self.left:
            self.left.rebalance()
            self.left = self.left.fix_imbalance()
        if self. right:
            self.right.rebalance()
            self.right = self.right.fix_imbalance()


def rotate_right(root: Node):
    pivot = root.left
    reattach_node = pivot.right
    root.left = reattach_node
    pivot.right = root
    return pivot


def rotate_left(root: Node):
    pivot = root.right
    reattach_node = pivot.left
    root.right = reattach_node
    pivot.left = root
    return pivot
