class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = 0    
        max_ = local = nums[0]
        
        for n in nums[1:]:
            sublocal = local + n
            local = n if local < 0 or sublocal < 0 else sublocal
            if local > max_:
                max_ = local
    
        return max_
