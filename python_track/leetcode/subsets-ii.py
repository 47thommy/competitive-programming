class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        visited=set()
        nums.sort()
        def backtrack(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
            backtrack(i+1)   
        backtrack(0)
        ans=[]
        for r in res:
            if r not in ans:
                ans.append(r)
        return ans