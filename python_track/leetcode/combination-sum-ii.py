class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:       
        candidates.sort()
        res=[]
        
        def backtrack(cur,idx,target):
            if target == 0:
                res.append(cur.copy())
            if target<=0:
                return
            prev=float('-inf')
            for i in range(idx,len(candidates)):
                if candidates[i]==prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur,i+1,target-candidates[i])
                cur.pop()
                prev=candidates[i]
        backtrack([],0,target)
        return res
