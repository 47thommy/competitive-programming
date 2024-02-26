# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def recursive(left,right):
            if left > right:
                return None
            mid=(left+right)//2
            left=recursive(left,mid-1)
            right=recursive(mid+1,right)
            return TreeNode(nums[mid],left,right)
        return recursive(0,len(nums)-1)