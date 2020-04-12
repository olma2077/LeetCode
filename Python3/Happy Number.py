class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n: True}
        
        while (n is not 1):
            n = sum([int(c) ** 2 for c in str(n)])
            if n in seen:
                return False
            else:
                seen[n] = True
        return True
