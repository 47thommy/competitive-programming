# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans=0
        def dfs(root):
            if p.val==root.val or q.val==root.val:
                self.ans=root
                return
            if (p.val < root.val and q.val >root.val) or (p.val > root.val and q.val <root.val):
                self.ans=root
                return
            if root.val>p.val:
                dfs(root.left)
            else:
                dfs(root.right)
            
        dfs(root)
        return self.ans

