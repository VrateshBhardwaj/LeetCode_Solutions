class Solution {
    public int divide(int dividend, int divisor) {
        long x =(long) dividend/divisor;
		int roundedNum =0;
        
        if(divisor==0)
        {
          System.out.println("Error cant divide by 0");
        }
		else if(x>=Integer.MAX_VALUE)
		{
			roundedNum =Integer.MAX_VALUE;
		
		}
		else {
		 roundedNum = (int) Math.floor(x);
		
		}
		return roundedNum;
		
    }
   
}