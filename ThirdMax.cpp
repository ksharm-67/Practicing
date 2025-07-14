class Solution {
public:
    int thirdMax(vector<int>& nums) {
        if(nums.size() == 1) return nums[0];
        if(nums.size() == 2) return nums[1];

        set<int> ns(nums.begin(), nums.end());

        for(auto n : ns){
            cout << n << " ";
        }

        vector<int> newNums(ns.begin(), ns.end());

        if(newNums.size() == 2) return newNums[1];
        else if(newNums.size() == 1) return newNums[0];
        return newNums[newNums.size() - 3];
    }
};