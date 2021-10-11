import unittest
from tree import Node
from LCA import lowest_common_ancestor

class TestLCA(unittest.TestCase):

    def test_same_node_search(self):
        root = Node("root")
        right = Node("right")
        left = Node("left")
        lr = Node("lr")
        ll = Node("ll")
        root.right = right
        root.left = left
        left.right = lr
        left.left = ll

        self.assertEqual(lowest_common_ancestor(ll, ll, root),"ll")

    def test_seperated_node_search(self):
        root = Node("root")
        right = Node("right")
        left = Node("left")
        lr = Node("lr")
        ll = Node("ll")
        root.right = right
        root.left = left
        left.right = lr
        left.left = ll

        self.assertEqual(lowest_common_ancestor(ll, right, root),"root")

    def test_parent_node_search(self):
        root = Node("root")
        right = Node("right")
        left = Node("left")
        lr = Node("lr")
        ll = Node("ll")
        root.right = right
        root.left = left
        left.right = lr
        left.left = ll

        self.assertEqual(lowest_common_ancestor(ll, left, root),"left")

    def test_children_node_search(self):
        root = Node("root")
        right = Node("right")
        left = Node("left")
        lr = Node("lr")
        ll = Node("ll")
        root.right = right
        root.left = left
        left.right = lr
        left.left = ll

        self.assertEqual(lowest_common_ancestor(ll, lr, root),"left")


if __name__ == '__main__':
    unittest.main()

