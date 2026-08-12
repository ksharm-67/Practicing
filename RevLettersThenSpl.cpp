class Solution {
public:
    string reverseByType(string s) {
        vector<char> letters, special;
        for(auto c : s){
            if(isalpha(c)) letters.push_back(c);
            else special.push_back(c);
        }

        reverse(letters.begin(), letters.end());
        reverse(special.begin(), special.end());

        string res = "";
        int currLet = 0, currSpl = 0;
        for(auto c : s){
            if(isalpha(c)) {
                res += letters[currLet];
                currLet += 1;
            }
            else {
                res += special[currSpl];
                currSpl += 1;
            }
        }

        return res;
    }
};
