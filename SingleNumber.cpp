class Solution {
public:
    int singleNumber(vector<int>& nums) {

        if(nums.size() == 1) return nums[0];

        unordered_map<int, vector<int>> mp;

        for(int i = 0; i < nums.size(); i++){
            mp[nums[i]].push_back(nums[i]);
        }

        for(auto itr : mp){
            if (itr.second.size() == 1) return itr.second[0];
        }
        return 0;
    }
};