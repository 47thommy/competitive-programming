class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        Current = 0
        maximum = 0
        for i in range(k):
            if s[i] in "aeiou":
                Current+=1
        maximum = max(maximum,Current)
        j = 0
        for i in range(k, len(s)):
            if s[i] in "aeiou":
                Current+=1
            if s[j] in "aeiou":
                Current-=1
            j+=1

            maximum = max(maximum,Current)
            
        return maximum