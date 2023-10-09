class Solution {
    public int[] searchRange(int[] nums, int target) {
        int first = first_val(nums, target);
        int last = last_val(nums, target);
        int[] result ={first, last};
        return result;
    }

    public int first_val(int[] nums, int target){
        int left = 0;
        int right = nums.length-1;
        int first = -1;

        while(left <= right){
            int mid = left+(right-left)/2;

            if(nums[mid]==target){
                first = mid;
                right = mid-1;
            }
            else if(nums[mid]<target)
            {
                left = mid+1;
            }
            else{
                right = mid-1;
            }
        }
        return first;
    }

    public int last_val(int[]nums, int target)
    {
        int left = 0;
        int right = nums.length-1;
        int last = -1;

        while(left<=right)
        {
            int mid = left+(right-left)/2;
            if(nums[mid]==target)
            {
                last = mid;
                left = mid+1;
            }
            else if(nums[mid]<target)
            {
                left = mid+1;
            }
            else{
              right = mid-1;
            }
        }
        return last;
    }
}