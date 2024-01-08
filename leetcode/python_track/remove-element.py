class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        left = 0

        for right in range(n):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1

        return left