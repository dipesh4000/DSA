class Solution {
    public int greater(int j, int[] nums){
        for(int i = j + 1; i < nums.length; i++){
            if(nums[i] > nums[j]){
                return nums[i];
            }
        }
        return -1;
    }

    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int[] ans = new int[m];

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(nums1[i] == nums2[j]){
                    ans[i] = greater(j, nums2);
                }
            }
        }
        return ans;
    }
}