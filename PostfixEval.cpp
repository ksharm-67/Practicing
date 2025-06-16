#include <iostream>
#include <stack>
#include <string>

using namespace std;

//Evaluate postfix expressions
int PostfixEval(string& s){

    stack<char> stk;

    for(int i = 0; i < s.size(); i++){
        if(s[i] == ' ' || ',') continue;

        else if(isdigit(s[i])){
            stk.push(s[i]);
        }

        //it is an operand
        else{
            int op1 = stoi(s[i]);
            stk.pop();

            int op2 = stoi(s[i]);
            stk.pop();
        }
    }
    return 1;
}

int main(){
    string k;
    cout << "Enter your postfix expression here: ";

    cin >> k;
    PostfixEval(k);
    return 1;
}