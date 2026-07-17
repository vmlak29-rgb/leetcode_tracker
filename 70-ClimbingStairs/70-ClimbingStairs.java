// Last updated: 17/07/2026, 15:03:00
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;

        int a = 1, b = 2;

        for (int i = 3; i <= n; i++) {
            b = a + b;
            a = b - a;
        }

        return b;
    }
}
