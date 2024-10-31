class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res_set = []

        for num in nums:
            if num % 3 == 0 and num % 2 == 0:
                res_set.append(num)
        
        return 0 if len(res_set) == 0 else sum(res_set) // len(res_set)

        