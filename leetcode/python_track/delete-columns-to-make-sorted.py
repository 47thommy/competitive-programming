class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        matrix=[]
        for s in strs:
            matrix.append(list(s))
        hashmap=defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                hashmap[j].append(matrix[i][j])
        for value in hashmap.values():
            if value!=sorted(value):
                count+=1
        return count