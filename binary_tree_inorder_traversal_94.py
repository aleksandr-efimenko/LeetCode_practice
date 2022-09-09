from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Left Root Right
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def in_traverse(root, result):
            if not root:
                return
            in_traverse(root.left, result)
            result.append(root.val)
            in_traverse(root.right, result)
        in_traverse(root, output)

        return output

