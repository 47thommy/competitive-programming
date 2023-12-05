class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        word = [(ele, idx) for idx, ele in enumerate(s)]
        
        word.sort(key = lambda ele : indices[ele[1]])
        word = [ele[0] for ele in word]
        ans= "".join(word)
        return ans