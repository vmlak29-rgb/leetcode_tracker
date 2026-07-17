// Last updated: 17/07/2026, 15:00:07
class Solution {
    public boolean hasAlternatingBits(int n) {
        String bits=Integer.toBinaryString(n);
        for(int i=0;i<bits.length()-1;i++){
            if(bits.charAt(i)==bits.charAt(i+1))
            {
                return false;
            }
        }
        return true;
    }
}

