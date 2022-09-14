import unittest
import pseudo_palindromic_paths_in_a_binary_tree_1457 as ps

class BT_Case(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.solution = ps.Solution()

    def test_pseudoPalindromicPaths_1(self):
        leaf1 = ps.TreeNode(val=3)
        leaf2 = ps.TreeNode(val=1)
        leaf3 = ps.TreeNode(val=1)
        node1 = ps.TreeNode(val=3, left=leaf1, right=leaf2)
        node2 = ps.TreeNode(val=1, right=leaf3)
        root = ps.TreeNode(val=2, left=node1, right=node2)
        expected = 2
        result = self.solution.pseudoPalindromicPaths(root)
        self.assertEqual(expected, result)

    def test_pseudoPalindromicPaths_2(self):
        node_4_1 = ps.TreeNode(val=1)
        node_3_1 = ps.TreeNode(val=1)
        node_3_2 = ps.TreeNode(val=3, right=node_4_1)
        node_2_1 = ps.TreeNode(val=1, left=node_3_1, right=node_3_2)
        node_2_2 = ps.TreeNode(val=1)
        node_1 = ps.TreeNode(val=1, left=node_2_1, right=node_2_2)
        expected = 2
        result = self.solution.pseudoPalindromicPaths(node_1)
        self.assertEqual(expected, result)

    def test_pseudoPalindromicPath_3(self):
        node = ps.TreeNode(val=9)
        expected = 1
        result = self.solution.pseudoPalindromicPaths(node)
        self.assertEqual(expected, result)