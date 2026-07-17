// Last updated: 17/07/2026, 15:00:39
class Solution {
    public boolean isPowerOfFour(int n) {
        if (n < 1) return false;
        if (n == 1) return true;
        while (n % 4 == 0) {
            n /= 4;
            if (n == 1) return true;
        }
        return false;
    }
}
