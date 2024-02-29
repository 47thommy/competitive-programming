# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        maximum=max(nums)
        maximumIndex=nums.index(maximum)
        newNode=TreeNode(nums[maximumIndex])
        newNode.left=self.constructMaximumBinaryTree(nums[:maximumIndex])
        newNode.right=self.constructMaximumBinaryTree(nums[maximumIndex+1:])
        return newNode

        