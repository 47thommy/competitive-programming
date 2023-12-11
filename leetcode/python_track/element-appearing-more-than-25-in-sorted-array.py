from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        appearance=len(arr)//4
        count=Counter(arr)
        print(count)
        for key in count:
            if count[key]>appearance:
                return key