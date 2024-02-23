# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        val1=p.val if p else None
        val2=q.val if q else None
        if val1!=val2:
            return False
        left = self.isSameTree(p.left if p else None,q.left if q else None)
        right = self.isSameTree(p.right if p else None,q.right if q else None)
        return left and right
