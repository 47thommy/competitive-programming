class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = 0
        res = 1
        for i, num in enumerate(nums):
            if num - nums[j] > k:
                res += 1
                j = i
        return res