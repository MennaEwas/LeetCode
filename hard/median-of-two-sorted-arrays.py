class Solution:
    def searchInsert(self, nums: List[int], target: int,priority) -> int:
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        while low <= high:
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            elif target == nums[mid]:
                if priority:
                    low = mid +1
                else:
                    high = mid -1
            mid = (low + high) // 2
        return mid + 1

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        needed = []
        med = []
        needed.append(n // 2)
        if n % 2 == 0:
            needed.append(n // 2 - 1)
        for i in range(len(nums1)):
            m = i + self.searchInsert(nums2, nums1[i],True)
            if m in needed:
                needed.remove(m)
                med.append(nums1[i])
        for i in range(len(nums2)):
            m = i + self.searchInsert(nums1, nums2[i],False)
            if m in needed:
                needed.remove(m)
                med.append(nums2[i])
        return sum(med) / len(med)
