// Last updated: 17/07/2026, 14:59:02
public class Solution {
    public boolean checkGoodInteger(int n) {
        int digitSum = 0;
        int squareSum = 0;
        while (n > 0) {
            int digit = n % 10;
            digitSum += digit;
            squareSum += digit * digit;
            n /= 10;
        }
        return (squareSum - digitSum) >= 50;
    }
}
