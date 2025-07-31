class Solution {
public:
    bool isGood(vector<int>& nums) {

        if(nums.size() == 1) return false;
        if(nums.size() == 2 && nums[0] == nums[1] && nums[0] == 1) return true;

        sort(nums.begin(), nums.end());
        if(nums[nums.size() - 1] != nums[nums.size() - 2]) return false;

        for(int i = 0; i < nums.size() - 1; i++){
            if(nums[i] != i + 1) return false;
        }

        return true;
    }
};