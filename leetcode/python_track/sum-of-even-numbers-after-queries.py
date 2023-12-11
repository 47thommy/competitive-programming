class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum=0
        ans=[]
        for num in nums:
            if num%2==0:
                even_sum+=num
        print(even_sum)
        for query in queries:
            initial_value=nums[query[1]]
            nums[query[1]]+=query[0]
            if nums[query[1]]%2==0 and initial_value%2==0:
                even_sum+=query[0]
            elif nums[query[1]]%2==0 and initial_value%2!=0:
                even_sum+=nums[query[1]]
            elif nums[query[1]]%2!=0 and initial_value%2!=0:
                even_sum+=0
            else:
                even_sum-=initial_value
            ans.append(even_sum)
        return ans