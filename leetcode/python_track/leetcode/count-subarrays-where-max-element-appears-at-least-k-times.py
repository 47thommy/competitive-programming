class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        answer = 0
        high = max(nums)
        count = 0

        left = 0
        for right in range(n):
            if nums[right] == high:
                count += 1
            while count >= k:
                answer += n - right
                if nums[left] == high:
                    count -= 1
                left += 1

        return answer
