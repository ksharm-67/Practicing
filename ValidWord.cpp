class Solution {
public:
    bool isValid(string word) {

        int vow = 0;
        int con = 0;

        transform(word.begin(), word.end(), word.begin(), ::tolower);

        for(char c : word){
            if(!isalpha(c) && !isdigit(c)) {return false;}
        }

        for(char w : word){
            if(w == 'a' || w == 'e' || w == 'i' || w == 'o' || w == 'u') {vow++; break;}
        }

        for(char t : word){
            if(isalpha(t) && (t != 'a' && t != 'e' && t != 'i' && t != 'o' && t != 'u')) {con++; break;}
        }

        return word.size() >= 3 && vow >= 1 && con >= 1;
        
    }
};