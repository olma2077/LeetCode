class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i+1:].count(target - nums[i]) > 0:
                return [i, nums.index(target - nums[i], i+1)]
        
