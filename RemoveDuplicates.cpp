#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//Remove duplicates from a sorted array; Solution is ~O(N^2) because I wanted to do it without using sets/maps

vector<int> removeSorted(vector<int>& nums){

    for(int i = 0; i < nums.size(); i++){
        for(int j = i + 1; j < nums.size(); j++){
            if(nums[i] == nums[j]){
                nums.erase(nums.begin() + j);
            }
        }
    }

    return nums;
}

int main(){

    //Modify this vector to anything you want it to be
    vector<int> array = {19, 2, 3, 4, 10, 4, 19, 59, 70, 1, 86};
    sort(array.begin(), array.end());

    vector<int> result = removeSorted(array);
    for(const auto& c : result){
        cout << c << " ";
    }
    cout << endl;
}