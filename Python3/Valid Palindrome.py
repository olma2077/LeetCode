class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('', '', string.punctuation + string.whitespace))
        s = s.lower()
        return s == s[::-1]
