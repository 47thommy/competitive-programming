# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        check=defaultdict(list)
        def dfs(x,y,node):
            if not node:
                return
            dfs(x-1,y+1,node.left)
            dfs(x+1,y+1,node.right)
            check[(x,y)].append(node.val)
        dfs(0,0,root)
        ans=[]
        prev=float("inf")
        for k,value in sorted(check.items()):
            if k[0]!=prev:
                ans.append([])
            ans[-1].extend(sorted(value))
            prev=k[0]
        return ans
