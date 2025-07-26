class Solution {
public:
    string reverseWords(string s) {
        
        bool word = false;
        string temp = "";
        vector<string> words;

        for(int k = s.size() - 1; k > 0; k--){
            if(s[k] == ' ') s.erase(k, 1);
            else break;
        }

        for(int i = 0; i < s.size(); i++){
            if(s[i] != ' '){
                word = true;
                temp += s[i];
            }
            else if(word){
                words.push_back(temp);
                temp = "";
                word = false;
            }
        }

        words.push_back(temp);
    
        string res;

        for(int j = words.size() - 1; j > 0; j--){
            res += words[j] += " ";
        }

        res += words[0];

        return res;
    }
};