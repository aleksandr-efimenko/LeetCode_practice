import unittest
import  binary_tree_inorder_traversal_94 as bt

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.solution = bt.Solution()

    @classmethod
    def tearDown(self) -> None:
        pass

    def test_inorderTraversal_3nodes(self):
        node3 = bt.TreeNode(val=3)
        node2 = bt.TreeNode(val=2, left=node3)
        node1 = bt.TreeNode(val=1, right=node2)
        expected = [1,3,2]
        result = self.solution.inorderTraversal(node1)
        self.assertEqual(expected, result)

    def test_inorderTraversal_5nodes(self):
        node5 = bt.TreeNode(val=5)
        node4 = bt.TreeNode(val=4)
        node3 = bt.TreeNode(val=3)
        node2 = bt.TreeNode(val=2, left=node4, right=node5)
        node1 = bt.TreeNode(val=1, left=node2, right=node3)
        expected = [4, 2, 5, 1, 3]
        result = self.solution.inorderTraversal(node1)
        self.assertEqual(expected, result)

    def test_inorderTraversal_0nodes(self):
        expected = []
        result = self.solution.inorderTraversal(None)
        self.assertEqual(expected, result)

    def test_inoderTraversal_1node(self):
        node1 = bt.TreeNode(val=1)
        expected = [1]
        result = self.solution.inorderTraversal(node1)
        self.assertEqual(expected, result)