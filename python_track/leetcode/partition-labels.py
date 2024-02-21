class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index={}
        for i in range(len(s)):
            last_index[s[i]]=i
        print(last_index)
        end=0
        size=0
        ans=[]
        for j in range(len(s)):
            size+=1
            end=max(end,last_index[s[j]])
            if j == end:
                ans.append(size)   
                size=0
        return ans
