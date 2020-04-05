class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = {}
        
        for i in nums:
            if i in res:
                del res[i]
            else:
                res[i] = True
                
        return list(res)[0]
