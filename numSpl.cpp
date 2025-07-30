class Solution {
public:
    int numberOfSpecialChars(string word) {
        
        if(word.size() == 1) return 0;
        
        sort(word.begin(), word.end());
        word.erase(std::unique(word.begin(), word.end()), word.end());
               
        int cnt = 0;
        int i = 0;
        size_t j = -1;

        while(i < word.size() && word[i] >= 65 && word[i] <= 90){
            j = word.find(char(word[i] + 32), i);
            if(j != string::npos) {
                cnt++;
            }
            i++;
        }
 
        return cnt;
    }
};