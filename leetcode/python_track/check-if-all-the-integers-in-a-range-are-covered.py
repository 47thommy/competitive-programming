class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        check=set()
        for i in range(left,right+1):
            check.add(i)
        for rang in ranges:
            for i in range(int(rang[0]), int(rang[-1])+1):
                if i in check:
                    check.discard(i)
        return len(check)==0
            