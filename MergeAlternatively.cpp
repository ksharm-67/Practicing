#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string shorter = "";
        
        if(word1.size() == word2.size() && word1.size() == 1) return shorter += word1 += word2;

        string res = "";  
        string longerString = "";
       
        if(word1.size() > word2.size()){
           shorter = word2;
           longerString = word1;
        }

        else{
            shorter = word1;
            longerString = word2;
        }

        for(int i = 0; i < shorter.size(); i++){
            res += word1[i];
            res += word2[i];
            longerString.erase(longerString.begin());
            
        }
        res += longerString;
        
        return res;
        
    }
};