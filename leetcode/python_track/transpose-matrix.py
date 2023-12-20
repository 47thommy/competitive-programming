from collections import defaultdict
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]
        hashmap=defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                hashmap[j].append(matrix[i][j])
        for value in hashmap.values():
            ans.append(value)
        return ans