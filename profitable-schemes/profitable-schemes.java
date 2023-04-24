        // n = weight of knapsack
        //group[] = weight[]
        //profit[] = values[]
        class Solution {
    private int mod = (int)1e9 + 7;
    public int profitableSchemes(int n, int minProfit, int[] group, int[] profit) {
        int dp[][] = new int[n+1][minProfit+1];
        dp[0][0] = 1;
        for(int job = 1; job <= group.length; job++) {
            int g = group[job-1];
            int p = profit[job-1];
            for(int weight = n; weight >= g; weight--) {
                for(int currProfit = minProfit; currProfit >= 0; currProfit--) {
                    dp[weight][currProfit] = (dp[weight][currProfit] + dp[weight-g][Math.max(0, currProfit-p)]) % mod;
                }
            }
        }
        int sum = 0;
        for(int i = 0; i <= n; i++) {
            sum = (sum + dp[i][minProfit]) % mod;
        }
        return sum;
    }
}
