// Last updated: 17/07/2026, 15:04:27
class Solution {
    public boolean isPalindrome(int x) {
        int rev = 0, temp = x;

        while (temp > 0) {
            rev = rev * 10 + temp % 10;
            temp = temp / 10;
        }

        return x == rev;
    }
}
