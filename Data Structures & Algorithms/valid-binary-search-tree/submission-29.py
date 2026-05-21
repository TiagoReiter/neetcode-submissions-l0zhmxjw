# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
1. A left subtree only contaisn values smaller than the nodes key
2. A right subtree only contaisn values larger than the nodes key
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return False
        def isValid(node, lower, upper):
            if not node:
                return True
            if not lower < node.val < upper:
                return False
            return isValid(node.left, lower, node.val) and isValid(node.right, node.val, upper)
        
        return isValid(root, float("-inf"), float("inf"))
