class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for k in d:
            if d[k] == 1:
                return s.index(k)
        return -1
