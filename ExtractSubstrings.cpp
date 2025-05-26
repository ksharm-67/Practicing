#include <iostream>
#include <vector>

using namespace std;

//Extract every second word from a sentence
string extract(string s){
    
    string result = "";
    int numWord;
    bool word;

    string temp = "";
    for(int i = 0; i < s.length(); i++){
        
        if(s[i] != ' ') {
            word = true;
            temp += s[i];
        }

        else if(word){
            numWord++;
            if(numWord % 2 == 0) result += temp + " ";
            temp = "";
            word = false;
        }
    }
    
    numWord++;
    if(word && numWord % 2 == 0) result += temp;

    return result;
}

int main(){

    //Change the sentence you want extracted here
    string sentence = "My name is Kavish Sharma . I am the best";

    cout << extract(sentence) << endl;

}