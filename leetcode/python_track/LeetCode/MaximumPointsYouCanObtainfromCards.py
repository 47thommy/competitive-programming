class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left=0
        ans=0
        check={}
        for end in range(len(nums)):
            check[nums[end]]=end
            if 
            while len(check.keys())>k:
                check[nums[left]]-=1
                if check[nums[left]]==0:
                    del check[nums[left]]
                left+=1
            ans+=end-left+1