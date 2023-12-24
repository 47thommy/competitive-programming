from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(list(s))
        ans=[]
        sort=count.most_common()
        for i in sort:
            x,y=i
            ans.append(x*y)
        return "".join(ans)
            