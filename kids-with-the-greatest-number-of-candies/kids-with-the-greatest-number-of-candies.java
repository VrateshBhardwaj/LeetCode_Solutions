class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
         List<Boolean> result = new ArrayList<>();
    int maxCandies = 0;
    
    // Find the maximum number of candies among all kids
    for (int i = 0; i < candies.length; i++) {
        if (candies[i] > maxCandies) {
            maxCandies = candies[i];
        }
    }
    
    // Check if each kid can have the greatest number of candies
    for (int i = 0; i < candies.length; i++) {
        if (candies[i] + extraCandies >= maxCandies) {
            result.add(true);
        } else {
            result.add(false);
        }
    }
    
    return result;
}
    }
