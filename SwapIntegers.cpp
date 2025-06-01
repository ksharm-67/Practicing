#include <iostream>

using namespace std;

//This function swaps two integers, using pointers
void swap(int* a, int* b){

    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(){
    int a, b;

    cout << "Enter a value for a: ";
    cin >> a;

    cout << "Enter a value for b: ";
    cin >> b;

    swap(&a, &b);
    cout << "Now, a is " << a << " and b is " << b << endl;

    return 1;
}
