class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        running_sum=0
        visited={0:1}
        count=0
        
        for i in range(len(nums)):
            running_sum+=nums[i]
            if running_sum%k in visited:
                count+=visited[running_sum%k]
            visited[running_sum%k]=visited.get(running_sum%k,0)+1
        print(visited)
        return count
            

                
                
                
            