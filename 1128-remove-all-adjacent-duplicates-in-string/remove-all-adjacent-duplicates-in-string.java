class Solution {
    // public String removeDuplicates(String s) {
    //     if(s.length() == 1) return s;
    //     Stack<Character> stack = new Stack<>();
    //     stack.push(s.charAt(0));
    //     for(int i = 1; i < s.length(); i++){
    //         if(!stack.empty() && stack.peek() == s.charAt(i)){
    //             stack.pop();
    //             continue;
    //         }
    //         stack.push(s.charAt(i));
    //     }
    //     StringBuilder sb = new StringBuilder();
    //     while(!stack.empty()){
    //         sb.append(stack.pop());
    //     }
    //     return sb.reverse().toString();
    // }
    public String removeDuplicates(String s) {
    StringBuilder sb = new StringBuilder();
    for (char c : s.toCharArray()) {
        int len = sb.length();
        // If the 'top' of the StringBuilder matches, 'pop' it
        if (len > 0 && sb.charAt(len - 1) == c) {
            sb.deleteCharAt(len - 1);
        } else {
            sb.append(c);
        }
    }
    return sb.toString();
}
}