// Last updated: 17/07/2026, 14:58:58
class Solution {
    public int maxDigitRange(int[] nums) {
        int maxRange=-1;
        int sum=0;
        for (int num:nums){
            int x=num;
            int maxDigit=0;
            int minDigit=9;
            while(x>0){
                int digit=x%10;
                maxDigit=Math.max(maxDigit,digit);
                minDigit=Math.min(minDigit,digit);
                x/=10;
            }
            int range=maxDigit-minDigit;
            if(range>maxRange){
                maxRange=range;
                sum=num;
            }else if(range==maxRange){
                sum+=num;
            }
            
            
        }
        return sum;
        
    }
}