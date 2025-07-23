class Solution {
public:
    bool sumOfNumberAndReverse(int num) {

        if(num == 0) return true;
        if(num == 1) return false;
        
        for(int i = num / 2; i < num; i++){

            string x = to_string(i);
            reverse(x.begin(), x.end());
            int rev = stoi(x);

            if(i + rev == num) return true;
        }

        return false;
    }
};