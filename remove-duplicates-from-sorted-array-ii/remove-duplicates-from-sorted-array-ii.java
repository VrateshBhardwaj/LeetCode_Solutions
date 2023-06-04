class Solution {
    public int removeDuplicates(int[] nums) {
        
        int size = nums.length;
        int k = 0;
		int removed = 0;

        for(int i = 0 ; i < size ; i++)
        {
            int frequency = 1;
            for(int j = i+1 ; j <= size-1 ; j++)
            {
                if(nums[i] == nums[j])
                {
                    frequency++;
                }
            }
            if(frequency > 2 && nums[i] == nums[i+1] )
            {             
            		nums[i] = nums[size-1];
                    nums[size-1] = nums[i];
                    removed ++;
            }
        }
        Arrays.sort(nums);
        k = size - removed;
        return k;
    }
}