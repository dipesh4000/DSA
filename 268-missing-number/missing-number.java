class Solution {
    public int missingNumber(int[] nums) {
      boolean[] seen = new boolean[nums.length + 1];
      for(int i: nums) {
        seen[i] = true;
      }
      for(int i = 0; i < seen.length; i++) {
        if(!seen[i]) return i;
      }


    return 0;  
    }
}