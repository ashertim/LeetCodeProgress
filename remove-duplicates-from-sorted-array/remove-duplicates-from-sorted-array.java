class Solution {
    public int removeDuplicates(int[] nums) {
        int firstInstance = 0;
        if (nums.length == 1)
            return 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[firstInstance]) {
                firstInstance++;
                nums[firstInstance] = nums[i];
            }
        }
        return ++firstInstance;
    }
}