class Solution {
public:
    string reverseWords(string s) {

        string res = "";
        bool word = false;

        string temp = "";

        for(int i = 0; i < s.size(); i++){
            if(s[i] != ' '){
                word = true;
                temp += s[i];
            }
            else if(word){
                reverse(temp.begin(), temp.end());
                res += temp += " ";
                temp = "";
                word = false;
            }
        }
        
        if(word && !temp.empty()) {
            reverse(temp.begin(), temp.end());
            res += temp;
        }

        return res;
    }
};