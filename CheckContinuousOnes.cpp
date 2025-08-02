class Solution {
public:
    bool checkOnesSegment(string s) {

        if(s.size() == 1 && s[0] == '0') return false;
        if(s.size() == 1 && s[0] == '1') return true;

        bool one = false;
        vector<string> seg;

        string temp = "";
        for(char c : s){
            if(c == '1'){
                one = true;
                temp += c;
            }
            else if(one){
                seg.push_back(temp);
                temp = "";
                one = false;
            }
        }

        if(one && !temp.empty()) seg.push_back(temp);
        
        return seg.size() == 1;
    }
};