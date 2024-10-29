class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        lss = -1
        lss_map = {}
        for num in nums:
            sq_rt = isqrt(num)
            if sq_rt in lss_map and sq_rt * sq_rt == num:
                lss_map[num] = lss_map[sq_rt] + 1
                lss = max(lss, lss_map[num])
            else:
                lss_map[num] = 1
        return lss

        