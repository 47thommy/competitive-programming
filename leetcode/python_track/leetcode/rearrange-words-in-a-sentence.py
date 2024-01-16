class Solution:
    def arrangeWords(self, text: str) -> str:
        
        words=text.split()
        words.sort(key=lambda x: len(x))
        lower=" ".join(words).lower()
        ans=lower.capitalize()
        return ans