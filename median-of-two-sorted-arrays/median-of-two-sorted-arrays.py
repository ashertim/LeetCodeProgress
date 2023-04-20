class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = sorted(nums1+nums2)
        length = len(combined)
        mid = int(len(combined)/2)
        if length % 2 == 0:
            return (combined[mid-1]+combined[mid])/2
        return combined[mid]