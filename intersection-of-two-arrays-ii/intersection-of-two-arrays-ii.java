class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        List<Integer> al = new ArrayList<>();

        // Count frequency of each element in nums1
        for (int i = 0; i < nums1.length; i++) {
            freqMap.put(nums1[i], freqMap.getOrDefault(nums1[i], 0) + 1);
        }

        // Update frequency counts and add common elements to al
        for (int i = 0; i < nums2.length; i++) {
            if (freqMap.containsKey(nums2[i]) && freqMap.get(nums2[i]) > 0) {
                al.add(nums2[i]);
                freqMap.put(nums2[i], freqMap.get(nums2[i]) - 1);
            }
        }

        // Convert ArrayList to int array
        int[] result = new int[al.size()];
        for (int i = 0; i < al.size(); i++) {
            result[i] = al.get(i);
        }
        return result;
    }
}
