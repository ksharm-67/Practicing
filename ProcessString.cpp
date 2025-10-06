class Solution {
public:
    string processStr(string s) {
        
        string res = "";
        for(int i = 0; i < s.size(); i++){
            if(res.empty() && (s[i] == '*')) continue;

            if(islower(s[i])) res += s[i];

            else if(s[i] == '*') res.pop_back();

            else if(s[i] == '#') res += res;

            else reverse(res.begin(), res.end());
        }

        return res;
    }
};
