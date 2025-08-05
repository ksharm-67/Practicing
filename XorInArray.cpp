class Solution {
public:
    int xorOperation(int n, int start) {
        
        int s = start;
        int el = start;

        for(int i = 1; i < n; i++){
            el = start + (2 * i);
            s ^= el;
        }
        return s;
    }
};