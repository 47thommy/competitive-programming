from collections import Counter
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        maxCount=float("-inf")
        hashmap={}
        ans=[]
        numsl=Counter(nums[:0])
        numsr=Counter(nums)
        nums1f=Counter(nums[0:])
        numsrf=Counter(nums[:0])
        for i in range(len(nums)):
            if i ==2:
                print(numsl,numsr)
            hashmap[i]=numsl[0]+numsr[1]
            if numsr[nums[i]]==0:
                del numsr[nums[i]]
            numsr[nums[i]]-=1
            numsl[nums[i]]=numsl.get(nums[i],0)+1
        hashmap[len(nums)]=nums1f[0]+numsrf[1]
        for key in hashmap:
            maxCount=max(maxCount,hashmap[key])
        listv=list(hashmap.values())
        listk=list(hashmap.keys())
        for k in range(len(listv)):
            if listv[k] == maxCount:
                ans.append(k)
        return ans
            