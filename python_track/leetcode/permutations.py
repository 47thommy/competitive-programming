class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        path=[]
        visited=set()
        def backtrack(num):
            if len(path)==len(nums):
                ans.append(path.copy())
                return
            for next_candidate in nums:
                if next_candidate not in visited:
                    path.append(next_candidate)
                    visited.add(next_candidate)
                    backtrack(next_candidate)
                    visited.remove(next_candidate)
                    path.pop()
                
        backtrack(nums[0])
        return ans