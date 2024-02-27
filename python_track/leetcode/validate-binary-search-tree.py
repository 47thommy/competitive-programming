# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, minimum, maximum):
            if root:
                if not minimum < root.val < maximum:
                    return False
                if not root.left and not root.right:
                    return True

                return dfs(root.left, minimum, root.val) and dfs(root.right, root.val, maximum)
            
            return True

        return dfs(root,float("-inf"),float("inf"))