class Solution:
    def myPow(self, x: float, n: int) -> float:

        def calculate_power(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return calculate_power(base * base, exponent // 2)
            else:
                return base * calculate_power(base * base, (exponent - 1) // 2)

        ans = calculate_power()
        
        return float(ans) if n >= 0 else 1/ans