#include <iostream>

using namespace std;

//Check if a given string is an exact palindrome or not
bool isPalindrome(string s){

    bool flag = true;

    for(int i = 0; i < s.length() / 2; i++){
        if(s[i] != s[s.length() - 1 - i]){
            flag = false;
        }
    }

    return flag;
}

int main(){

    //Change this to the string you want to check is a palindrome
    string pal = "madam";

    //1: it is a palindrome, 0: it is not a palindrome
    cout << isPalindrome(pal) << endl;
    return 0;
}