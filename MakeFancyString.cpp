class Solution {
public:
    string makeFancyString(string s) {
        string res;
        for (char c : s) {
            int n = res.size();
            if (n >= 2 && res[n - 1] == c && res[n - 2] == c) continue;
            res.push_back(c);
        }
        return res;
    }
};
