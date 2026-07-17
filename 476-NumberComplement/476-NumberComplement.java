// Last updated: 17/07/2026, 15:00:32
class Solution {
    public int findComplement(int num) {
        int mask = 1;
        while (mask < num) {
            mask = (mask << 1) | 1;
        }
        return num ^ mask;
    }
}
