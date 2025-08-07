
class Solution {
public:
    int countDigits(int num) {
        
        int count = 0;
        string n = to_string(num);

        for(int i = 0; i < n.size(); i++){
            if(num % (n[i] - '0') == 0) count++;
        }

        return count;
    }
};