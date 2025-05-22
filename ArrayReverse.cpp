#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int> nums;
    int a, i;

    cout << "Enter anything other than a number to terminate input." << endl;

    while(cin >> a){
        nums.push_back(a);
    }

    cout << "{";

    for(i = nums.size() - 1; i >= 0; i--){
        cout << nums[i] << " ";
    }

    cout << "}\n";
}