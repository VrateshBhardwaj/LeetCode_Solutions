class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        Arrays.sort(arr);

        int diffOfFirstTwo = arr[0]-arr[1];
        boolean isAP = true;
        for(int i=1; i<arr.length-1; i++)
        {
            int j = i+1;

            int currDiff = arr[i]-arr[j];
            if(diffOfFirstTwo != currDiff)
            {
                isAP = false;
                break;
            } 
        }
        return isAP;
    }
}