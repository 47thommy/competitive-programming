class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

    
        def postOrder(node):
            if not node.left and not node.right:
                self.ans = max(self.ans, node.val)
                return node.val, node.val, node.val

            leftSum, leftMin, leftMax = 0, node.val, -math.inf
            if node.left:
                leftSum, leftMin, leftMax = postOrder(node.left)

            rightSum, rightMin, rightMax = 0, math.inf, node.val
            if node.right:
                rightSum, rightMin, rightMax = postOrder(node.right)

            if leftMax < node.val < rightMin:
                currSum = leftSum + node.val + rightSum
                self.ans = max(self.ans, currSum)
                return currSum, leftMin, rightMax
            else:
                return 0, float('-inf'), float("inf")
        
        postOrder(root)
        return self.ans