#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

//Optimized TwoSum using map
vector<int> TwoSum(vector<int> nums, int target){
    unordered_map<int, int> freq;

    for(int i = 0; i < nums.size(); i++){
        int complement = target - nums[i];

        auto itr = freq.find(complement);
        if(itr != freq.end()){
            return {i, itr->second};
        }

        else{
            freq[nums[i]] = i;
        }
    }
    return {-1, -1};
}

int main(){

    //Enter the numbers you want into this vector
    vector<int> nums = {1, 3, 4, 2, 6, 9, 8, 7, 10};

    //Target number which the elements should add upto
    int tar = 16;

    vector<int> res = TwoSum(nums, tar);
    for(int i = 0; i < res.size(); i++){
        cout << res[i] << " ";
    }
    cout << endl;
}
