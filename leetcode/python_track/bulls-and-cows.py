from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        check=Counter(secret)-Counter(guess)
        bulls_count=0
        print(check)
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls_count+=1
        cows_count=len(secret)-sum(check.values())-bulls_count
        return str(bulls_count)+"A"+str(cows_count)+"B"