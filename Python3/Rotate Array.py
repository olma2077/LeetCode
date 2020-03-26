class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        shift = k % len(nums)
        for i, n in enumerate([*nums[-shift:], *nums[:-shift]]):
            nums[i] = n
