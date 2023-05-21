class Solution {
    public int removeDuplicates(int[] nums) {
			ArrayList<Integer> al  = new ArrayList<Integer>();
		Arrays.sort(nums);
		
		int k=0;
		for(int i = 0;i<=nums.length-1;i++)
		{
			if(!al.contains(nums[i]))
				{
				al.add(nums[i]);
				}
			 
		}
		for(int i=0;i<al.size();i++)
		{
			nums[i] = al.get(i);
		}
		 return k = al.size();
		}
}