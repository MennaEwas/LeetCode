class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        a = 0 
        b = 0
        if len(nums1) > len(nums2):
            a = len(nums1)
        else:
            b = len(nums2)
        
        if a:
            for it in nums2:
                if it in nums1:
                    l.append(it)
                    nums1.remove(it)
        else:
            for it in nums1:
                if it in nums2:
                    l.append(it)
                    nums2.remove(it)
                    
                    
        return list(set(l))
            