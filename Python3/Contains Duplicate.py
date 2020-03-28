class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = set()
        for i in nums:
            if i in store:
                return True
            else:
                store.add(i)
        return False
