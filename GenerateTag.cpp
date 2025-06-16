#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string generateTag(string caption) {
    string fin = "";
    string res = "";
    fin += tolower(caption[0]);
    
    for(int i = 1; i < caption.size(); i++){
        if(caption[i-1] == ' '){
            char c = toupper(caption[i]);
            fin += c;
        }
        else{
            fin += tolower(caption[i]);
        }
    }

    fin.erase(remove(fin.begin(), fin.end(), ' '), fin.end());
    fin[0] = tolower(fin[0]);

    for(int j = 0; j < fin.size() && res.size() < 99; j++) {
        res += fin[j];
    }

    return '#' + res;
}