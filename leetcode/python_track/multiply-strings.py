class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len1, len2 = len(num1), len(num2)
        product = [0] * (len1 + len2)
        
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                product[i + j + 1] += digit1 * digit2
                product[i + j] += product[i + j + 1] // 10
                product[i + j + 1] %= 10
        
        result = ''.join(str(i) for i in product).lstrip('0')
        return result if result else '0'
