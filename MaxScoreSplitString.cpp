class Solution {
public:
    int maxScore(string s) {
        int left = 0;
        unordered_map<char, int> mp;
        
        for(int i = 1; i < s.size(); i++) {
            if(s[i] == '1') mp[s[i]] += 1;
        }
        
        int maxScore = 0;
        for(int j = 1; j < s.size(); j++) {
            if(s[j - 1] == '0') mp['0'] += 1;

            maxScore = max(maxScore, mp['0'] + mp['1']);

            if(s[j] == '1') mp['1'] -= 1;
        }

        return maxScore;
    }
};
