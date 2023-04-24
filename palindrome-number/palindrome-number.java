class Solution {
    public static boolean isPalindrome(int x) {
        int rev=0;
       int temp=x;
       boolean str = true;
        while(temp>0)
        {
         int rem =temp%10;//end digit
        
         rev = rev*10+rem;
         temp=temp/10;
         
        }
        System.out.println(rev);
        if( x!=rev){
            str = false;
        }
        else{
            str= true;
        }
       return str;
    }
}