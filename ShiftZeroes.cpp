#include <iostream>
#include <vector>

using namespace std;

//Shifts all zeroes to the end of the array without creating another array
vector<int> ShiftZeroes(vector<int>& list){

    for(int i = list.size() - 1; i >= 0; i--){
        if(list[i] == 0){
            list.erase(list.begin() + i);
            list.push_back(0);
        }
    }
    
    return list;
}

int main(){

    //Add any elements to this vector
    vector<int> v = {0, 5, 7, 1, 6, 0, 0, 1, 0, 3};

    vector<int> result = ShiftZeroes(v);
    for(const auto& c : result){
        cout << c << " ";
    }
    
    cout << endl;
}