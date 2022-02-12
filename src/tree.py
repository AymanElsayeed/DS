"""

    Tree Module

"""
from src.node import Node

__all__ = ['Tree', 'Node']


class Tree:
    def __init__(self, root: Node, name=''):
        self.root = root
        self.name = name

    def rebalance(self):
        self.root.rebalance()
        self.root = self.root.fix_imbalance()

    def delete(self, target):
        self.root = self.root.delete(target=target)

    def insert(self, data):
        self.root.insert(data=data)
        self.root = self.root.fix_imbalance()

    def search(self, target):
        return self.root.search(target=target)

    def traverse_preorder(self):
        self.root.traverse_preorder()

    def traverse_inorder(self):
        self.root.traverse_inorder()

    def traverse_postorder(self):
        self.root.traverse_postorder()

    def height(self):
        return self.root.height()

    def get_node_at_depth(self, depth):
        return self.root.get_node_at_depth(depth=depth)

    def _node_to_char(self, n, spacing):
        if n is None:
            return '_' + (' ' * spacing)
        spacing = spacing - len(n.to_str()) + 1
        return n.to_str() + (' ' * spacing)

    def print(self, label=''):
        print(self.name + ' ' + label)
        height = self.root.height()
        spacing = 3
        width = int((2 ** height - 1) * (spacing + 1) + 1)
        # Root offset
        offset = int((width - 1) / 2)
        for depth in range(0, height + 1):
            if depth > 0:
                # print directional lines
                print(' ' * (offset + 1) + (' ' * (spacing + 2)).join(
                    ['/' + (' ' * (spacing - 2)) + '\\'] * (2 ** (depth - 1))))
            row = self.root.get_node_at_depth(depth, [])
            print((' ' * offset) + ''.join([self._node_to_char(n, spacing) for n in row]))
            spacing = offset + 1
            offset = int(offset / 2) - 1
        print('')