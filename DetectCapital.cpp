class Solution {
public:
    bool detectCapitalUse(string word) {
        int cntCap = 0;
        int cntLow = 0;

        for(char w : word){
            if (isupper(w)) {
                cntCap++;
            }
            else{
                cntLow++;
            }
        } 
        if (cntCap > 0 && cntLow == 0) return true;
        else if(cntCap == 0 && cntLow > 0) return true;
        else if(isupper(word[0]) && cntLow == word.size() - 1) return true;

        return false;
    }
};