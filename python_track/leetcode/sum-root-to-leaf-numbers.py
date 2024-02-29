# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def preorder(cur,num):
            if not cur:
                return 0

            num=num*10 + cur.val
            
            if not cur.left and not cur.right:
                return num

            return preorder(cur.left, num) + preorder(cur.right,num)

        return preorder(root,0)
        