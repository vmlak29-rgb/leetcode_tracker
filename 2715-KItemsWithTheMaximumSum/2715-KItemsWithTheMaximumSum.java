// Last updated: 17/07/2026, 14:59:08
class Solution {
    public int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        int onesTaken = Math.min(k, numOnes);
        k -= onesTaken;

        int zerosTaken = Math.min(k, numZeros);
        k -= zerosTaken;

        int negOnesTaken = k;

        return onesTaken - negOnesTaken;
    }
}
