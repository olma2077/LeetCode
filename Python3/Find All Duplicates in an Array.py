class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            if nums[abs(i)-1] > 0:
                nums[abs(i)-1] = -nums[abs(i)-1]
            else:
                result.append(abs(i))
        return result
