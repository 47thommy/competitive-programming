class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        min_difference = float('inf')

        for i in range(len(nums) - 1):
            difference = nums[i + 1] - nums[i]
            min_difference = min(min_difference, difference)

        return min_difference