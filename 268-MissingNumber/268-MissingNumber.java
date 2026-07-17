// Last updated: 17/07/2026, 15:00:51
class Solution {
    public int missingNumber(int[] nums) {
        int n=nums.length;
        int total=n*(n+1)/2;
        int sum=0;
        for(int num :nums){
            sum+=num;
        }
        return total-sum;
        
    }
}