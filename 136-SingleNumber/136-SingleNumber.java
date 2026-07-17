// Last updated: 17/07/2026, 15:01:47
class Solution {
    public int singleNumber(int[] nums) {
        int result = 0;
        for (int x : nums) {
            result ^= x;
        }

        return result;
    }
}
