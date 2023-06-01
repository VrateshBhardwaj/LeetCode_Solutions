class Solution {
   public static boolean isValid(String s)
	{
		Stack<Character> stk = new Stack<Character>();
		

        HashMap<Character, Character> map = new HashMap<Character, Character>();
        map.put('(', ')');
        map.put('{', '}');
        map.put('[', ']');

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (map.containsKey(ch)) {
                stk.push(ch);
            } else if (map.containsValue(ch)) {
                if (stk.isEmpty() || ch != map.get(stk.pop())) {
                    return false;
                }
            }
        }

        return stk.isEmpty();
    }
  }
