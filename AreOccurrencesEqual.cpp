class Solution {
public:
    bool areOccurrencesEqual(string s) {
        
        unordered_map<char, int> mp;

        for(int i = 0; i < s.size(); i++){
            mp[s[i]]++;
        }

        int freq = mp.begin()->second;

        for(auto m : mp){
            if(m.second != freq) return false;
        }

        return true;
    }
};