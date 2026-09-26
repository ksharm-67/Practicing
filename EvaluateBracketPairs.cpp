class Solution {
public:
    string evaluate(string s, vector<vector<string>>& knowledge) {
        unordered_map<string, string> dict;
        for(auto& k : knowledge) dict[k[0]] = k[1];
        
        string key = "", res = "";
        bool open = false;
        for(int i = 0; i < s.size(); i++) {
            if(s[i] == '(') {
                open = true;
            }
            else if(s[i] == ')') {
                if(dict.find(key) != dict.end()) {
                    res += dict[key];
                }
                else res += '?';
                open = false;
                key = "";
            }
            else if(open) {
                key += s[i];
            }
            else {
                res += s[i];
            }
        }

        return res;
    }
};
