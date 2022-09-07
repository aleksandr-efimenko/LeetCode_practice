from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree2str(root: Optional[TreeNode]) -> str:
    if root is None:
        return ''
    if root.left is None and root.right is None:
        return str(root.val)
    if root.right is None:
        return f'{str(root.val)}({tree2str(root.left)})'
    return f'{str(root.val)}({tree2str(root.left)})({tree2str(root.right)})'
