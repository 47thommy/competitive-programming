class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number=0
        for letter in columnTitle:
            number=number*26 + (ord(letter)-64)
        return number