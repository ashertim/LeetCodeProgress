class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for nd in nums2:
            nums1[m] = nd
            m+=1
        nums1.sort()
                    


        