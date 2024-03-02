class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []

        def inOrder(node):
            if not node:
                return 

            inOrder(node.left)
            nums.append(node.val)
            inOrder(node.right)

        inOrder(root)

        def balance(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = balance(left, mid - 1)
            node.right = balance(mid + 1, right)

            return node

        return balance(0,len(nums) - 1) 