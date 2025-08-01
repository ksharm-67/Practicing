class Solution {
public:
    string largestOddNumber(string num) {
    
        if(num.size() == 1 && (num[0] - '0') % 2 == 1) return num;
        if(num.size() == 1 && (num[0] - '0') % 2 == 0) return "";

        for(int i = num.size() - 1; i >= 0; i--){
            if((num[i] - '0') % 2 == 1) return num.substr(0, i + 1);
        }

        return "";
    }
};