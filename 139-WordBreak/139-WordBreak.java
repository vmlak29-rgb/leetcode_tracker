// Last updated: 17/07/2026, 15:01:46
class Solution {
   boolean[] memo;
   public boolean wordBreak(String s, List<String> wordDict) {
       memo = new boolean[s.length() + 1];
       return wordBreak(s, wordDict, 0);
   }
   boolean wordBreak(String s, List<String> wordDict, int k) {
       if (k == s.length())
           return true;
       
       if (memo[k])
           return false;
       
       for (String word : wordDict) {
           if (s.startsWith(word, k)) {
               memo[k] = true;
               if(wordBreak(s, wordDict, k + word.length())) return true;
           }
       }    
       return false;
   }
}