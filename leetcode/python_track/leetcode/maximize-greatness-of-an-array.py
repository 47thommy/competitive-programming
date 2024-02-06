class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for num in nums:

            if nums[i] < num:
                i += 1
        return i
