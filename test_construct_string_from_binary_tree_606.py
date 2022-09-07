import unittest
import construct_string_from_binary_tree_606 as ct

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        pass
    @classmethod
    def tearDown(self) -> None:
        pass

    def test_tree2str(self):
        node4 = ct.TreeNode(val=4)
        node2 = ct.TreeNode(val=2, left=node4)
        node3 = ct.TreeNode(val=3)
        root = ct.TreeNode(val=1, left=node2, right=node3)

        result = ct.tree2str(root)
        expected = '1(2(4))(3)'
        self.assertEqual(expected, result)  # add assertion here

    def test_tree2str_(self):
        node4 = ct.TreeNode(val=4)
        node2 = ct.TreeNode(val=2, right=node4)
        node3 = ct.TreeNode(val=3)
        root = ct.TreeNode(val=1, left=node2, right=node3)

        result = ct.tree2str(root)
        expected = '1(2()(4))(3)'
        self.assertEqual(expected, result)  # add assertion here

    def test_tree2str_empty(self):
        self.assertEqual(ct.tree2str(None), '')




if __name__ == '__main__':
    unittest.main()
