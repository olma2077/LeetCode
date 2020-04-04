class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        digits[-1] = (digits[-1] + 1) % 10
        if digits[-1] == 0:
            digits = self.plusOne(digits=digits[:-1])
            digits.append(0)
        return digits
