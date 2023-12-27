from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        set2=set(arr2)
        count=Counter(arr1)
        ans=[]
        for n in arr2:
            for i in range(count[n]):
                ans.append(n)
            del count[n]
        
        rest=[]
        for key in count:
            for j in range(count[key]):
                rest.append(key)
        for k in range(len(rest)):
            for l in range(len(rest)-1):
                if rest[l]>rest[l+1]:
                    rest[l],rest[l+1]=rest[l+1],rest[l]
        
        for e in rest:
            ans.append(e)
        return ans