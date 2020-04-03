class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr1 = nums2 if len(nums1) < len(nums2) else nums1
        arr2 = nums2 if len(nums1) >= len(nums2) else nums1
        res = []
        
        for i in arr1:
            if i in arr2:
                res.append(i)
                arr2.remove(i)
                if len(arr2) == 0:
                    break
        
        return res
