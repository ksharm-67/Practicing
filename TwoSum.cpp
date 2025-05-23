#include <iostream>
#include <vector>
using namespace std;

//Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

vector<int> twoSum(vector<int>& nums, int target){
    vector<int> pair(2);

    for(int i = 0; i < nums.size(); i++){
        for(int j = i + 1; j < nums.size(); j++){
            if (nums[i] + nums[j] == target) {
                pair[0] = i;
                pair[1] = j;
            } 
        }
    }
    return pair;
}

int main(){
    //Edit this vector with any numbers you want. No repetition. 
    vector<int> nums = {1, 4, 5, 18, 4, 8};

    //Target can be any integer you want.
    int target = 8;

    vector<int> indices = twoSum(nums, target);
    cout << indices[0] << ", " << indices[1] << endl;
}