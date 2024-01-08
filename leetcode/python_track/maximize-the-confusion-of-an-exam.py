class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        T = -1
        F=-1
        
        k2 = 0
        i = 0
        for j in range(len(answerKey)):
            if answerKey[j] != "T":
                k2 += 1
            while k2 > k:
                if answerKey[i] != "T":
                    k2 -= 1
                i += 1
            T = max(j - i + 1, T)
            
            
        k2=0
        i=0
        for j in range(len(answerKey)):
            if answerKey[j] != "F":
                k2 += 1
            while k2 > k:
                if answerKey[i] != "F":
                    k2 -= 1
                i += 1
            F = max(j - i + 1, F)  
            
            
        return max(T, F)
        
    