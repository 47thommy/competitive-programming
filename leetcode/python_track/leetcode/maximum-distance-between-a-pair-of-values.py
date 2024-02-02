class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0 
        max_distance = 0
        while i < len(nums1) and j < len(nums2):   
            if nums1[i] <= nums2[j]:
                max_distance = max(max_distance, j - i)
                j += 1
            else:
                i += 1
                if i > j:
                    j = i
        return max_distance