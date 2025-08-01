class Solution {
public:
    int smallestNumber(int n, int t) {

        while(true){
            int prod = 1;
            int temp = n;

            while(temp > 0){
                int last = temp % 10;
                prod *= last;
                temp /= 10;
            }

            if(prod % t == 0) return n;
            else n += 1;
        }
        return 0;
    }
};