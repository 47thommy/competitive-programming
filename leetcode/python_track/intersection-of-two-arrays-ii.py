from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1=Counter(nums1)
        count2=Counter(nums2)
        ans=[]
        for i in range(len(nums1)):
            if nums1[i] in count2:
                if (count1[nums1[i]]>=count2[nums1[i]]):
                    j=count2[nums1[i]]
                    while j>0:
                        ans.append(nums1[i])
                        j-=1
                    del count2[nums1[i]]
                else:
                    j=count1[nums1[i]]
                    while j>0:
                        ans.append(nums1[i])
                        j-=1
                    del count1[nums1[i]]
                   
        return ans
            
        