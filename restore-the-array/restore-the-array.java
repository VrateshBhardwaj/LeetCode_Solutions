class Solution {
    public int dfs(String s, long k,int i,int[]dp)
    {
        if(i==s.length())
        {
            return 1;
        }
        if(s.charAt(i)=='0')
        {
            return 0;
        }
        if(dp[i]!=-1)
        {
            return dp[i];
        }
        long no = 0;
        int answer = 0;
        for(int j=i;j<s.length();j++)
        {
            no = no * 10+ s.charAt(j) - '0';

            if(no>k)
            {
                break;
            }
            answer = (answer +dfs(s,k,j+1,dp)) % 1000000007;

        }
        return dp[i] = answer;

    }
    public int numberOfArrays(String s, int k) {
   int dp [] = new int [s.length()];
   Arrays.fill(dp,-1);
   return dfs(s,k,0,dp);
    }
    
}