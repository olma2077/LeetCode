class Solution:
    def reverse(self, x: int) -> int:
        l = list(str(abs(x)))
        l.reverse()
        rx = int("".join(l)) if x > 0 else -int("".join(l))
        return rx if (rx < ((2 ** 31) - 1) and rx > -(2 ** 31)) else 0
