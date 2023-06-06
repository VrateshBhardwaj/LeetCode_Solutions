class Solution {
    public int majorityElement(int[] nums) {
        int count = 1;
        int candidate = 0;
        int element = -1;
        for(int i=0;i<nums.length;i++)
        {
           if(nums[candidate] == nums[i])
           {
               count++;
           }
           else{
               count--;
           }

           if(count==0)
           {
               candidate = i;
               count = 1;
           }
        }
      return nums[candidate];
    }
}