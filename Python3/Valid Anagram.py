class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls, lt = list(s), list(t)
        ls.sort()
        lt.sort()
        return ls == lt
