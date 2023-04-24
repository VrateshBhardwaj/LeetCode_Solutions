class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if(nums2.length==0)
        {
            for(int i=0;i<nums1.length;i++)
            {
                System.out.println (nums1[i]);
            }
        }
       HashMap <Integer,Integer> map = new HashMap<>();//cfreates a new hash map
       for(int i=0;i<nums2.length;i++)
       {
           map.put(n+1,nums2[i]);//stores the value of nums2 and their key as nums2.length+1
           n++;
       }
       int i=0;
       for(Map.Entry<Integer,Integer> entry: map.entrySet())
       {
          
           int val = entry.getValue();
           int key = entry.getKey();
           nums1[m+i] = val;
           i++;
        
       }
        Arrays.sort(nums1);
        }
    }
