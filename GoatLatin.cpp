class Solution {
public:
    string toGoatLatin(string sentence) {
        
        vector<string> words;

        string temp = "";
        bool inWord = false;

        for(char s : sentence){
            if(s != ' '){
                inWord = true;
                temp += s;
            }
            else if(inWord){
                words.push_back(temp);
                temp = "";
                inWord = false;
            }
        }
        words.push_back(temp);

        for(int x = 0; x < words.size(); x++){
            if(char lower = tolower(words[x][0]); 
            lower != 'a' && lower != 'e' && lower != 'i' && lower != 'o' && lower != 'u'){
                char temp = words[x][0];
                words[x].erase(words[x].begin());
                words[x] += temp;
            }
            
            words[x] += "ma";
            string repeated(x + 1, 'a');
            words[x] += repeated;

            cout << words[x] << " ";
        }

        string res = "";
        for(string i : words) res += i += " ";
        res.erase(res.size() - 1);

        return res;
    }
};