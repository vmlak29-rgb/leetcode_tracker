// Last updated: 17/07/2026, 14:59:09
class Solution {
    public int passThePillow(int n, int time) {
        int pos = 1, dir = 1;
        for (int i = 0; i < time; i++) {
            pos += dir;
            if (pos == n || pos == 1) dir = -dir;
        }
        return pos;
    }
}
