#include <iostream>
#include <string>

using namespace std;

//Find the string (needle) in another, longer string (haystack) and return the index of 1st occurence
int IndexFirstOccur(const string& haystack, const string& needle){

    if(needle.length() > haystack.length()) return -1;
    if(needle.empty()) return -1;

    for(int i = 0; i < haystack.length(); i++){
        if(haystack.substr(i,needle.length()) == needle) return i;
    }

    return -1;
}

int main(){

    string needle, haystack;

    cout << "Enter what you want to find a string in (haystack): ";
    cin >> haystack;

    cout << "Enter what you want to find (needle):  ";
    cin >> needle;

    int index = IndexFirstOccur(haystack, needle);

    cout << "Found at index " << index << endl;
    return 1;
}