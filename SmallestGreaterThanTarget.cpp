class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        set<char> ls;
        for(char c : letters){
            if(c > target) ls.insert(c);
        }
        
        if(!ls.empty()) return *ls.begin();
        
        return letters[0];
    }
};
