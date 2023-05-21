class Solution {
    public int removeDuplicates(int[] nums) {
        
		ArrayList<Integer> al  = new ArrayList<Integer>();
		Arrays.sort(nums);
		int c = 0;
		int k=0;
		for(int i = nums.length-1;i>=0;i--)
		{
			if(i == nums.length-1 || nums[i] != nums[i+1])
				{
				al.add(nums[i]);
				}
			 
		}
		al.sort(null);
		System.out.println(al);
		
		for(int i=0;i<al.size();i++)
		{
			nums[i] = al.get(i);
		}
		
		 return k = al.size();
		
    }
}