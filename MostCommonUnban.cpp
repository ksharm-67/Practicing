class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        
        map<string, int> mp;

        bool word = false;
        string temp = "";

        for(int i = 0; i < paragraph.size(); i++){
            if(paragraph[i] != ' ' && !ispunct(paragraph[i])){
                word = true;
                temp += paragraph[i];
            }
            else if(word){
                transform(temp.begin(), temp.end(), temp.begin(), ::tolower);
                auto itr = find(banned.begin(), banned.end(), temp);

                if(itr == banned.end()) mp[temp]++;
                temp = "";
                word = false;
            }   
        }

        if(word) {
            transform(temp.begin(), temp.end(), temp.begin(), ::tolower);
            auto itr = find(banned.begin(), banned.end(), temp);
            if(itr == banned.end()) mp[temp]++;
        }

        string maxWord;
        int maxFreq = 0;

        for(auto& [word, freq] : mp){
            if(freq > maxFreq){
                maxFreq = freq;
                maxWord = word;
            }
        }

        return maxWord;
    }
};
