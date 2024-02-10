class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        total_sum = sum(nums)
        remainder = total_sum % p

        if remainder == 0:
            return 0

        prefix_remainder = 0
        rightmost_remainder_indices = {0: -1}
        min_subarray_length = len(nums)

        for i, num in enumerate(nums):

            prefix_remainder = (prefix_remainder + num) % p

            required_remainder = (prefix_remainder - remainder) % p

            if required_remainder in rightmost_remainder_indices:
                j = rightmost_remainder_indices[required_remainder]
                min_subarray_length = min(min_subarray_length, i - j)

            rightmost_remainder_indices[prefix_remainder] = i

        return min_subarray_length if min_subarray_length < len(nums) else -1
