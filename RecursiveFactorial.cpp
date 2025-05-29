#include <iostream>

using namespace std;

//Recursively find the factorial of a number
int RecursiveFactorial(int n){
    if(n == 0){
        return 1;
    }
    
    else{
        return n * RecursiveFactorial(n-1);
    }
}

int main(){
    int a;
    cout << "Enter number here: " << endl;
    cin >> a;

    cout << "Factorial = " << RecursiveFactorial(a) << endl;

    return 1;
}