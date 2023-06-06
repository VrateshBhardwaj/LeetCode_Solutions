class Solution {
    public int maximumWealth(int[][] accounts) {
        int sum = 0;
		for(int i=0;i<accounts.length;i++)
		{
			int currSum=0;
			for(int j=0;j<accounts[0].length;j++)
			{
				 
				 currSum += accounts[i][j];
				 sum = Math.max(sum, currSum);
			}
		}
		return sum;
    }
}