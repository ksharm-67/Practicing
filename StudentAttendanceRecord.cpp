#include <iostream>
#include <algorithm>
#include <string>

class Solution {
public:
    bool checkRecord(string s) {

        if(count(s.begin(), s.end(), 'A') >= 2) return false;
        
        for(int i = 2; i < s.size(); i++){
            if(s[i] == 'L' && s[i-1] == 'L' && s[i-2] == 'L') return false;
        }

        return true;
    }
};