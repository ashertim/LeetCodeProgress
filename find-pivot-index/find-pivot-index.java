class Solution {
    public int pivotIndex(int[] nums) {
        int left = 0, index = 0;
        int right = -nums[0];
        for (int num : nums)
            right += num;
        
        while (left != right) {
            if (index == nums.length-1)
                return -1;
            left += nums[index];
            index++;
            right -= nums[index];
        }

        return index;
    }
}