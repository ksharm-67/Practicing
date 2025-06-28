#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool rotateString(string s, string goal) {
        if(s == goal) return true;

        string copy = s;
        
        for(int i = 0; i < s.size(); i++){

            cout << copy << endl;

            char rem = copy[0];
            copy.erase(copy.begin());
            copy += rem;

            cout << copy << endl;
            
            if(copy == goal) return true;
        }
        
        return false;
    }
};