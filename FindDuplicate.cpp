class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        for(int i = 0; i < nums.size(); i++){
            int ind = abs(nums[i]);
            if(nums[ind] < 0) return ind;
            nums[ind] *= -1;
        }
        return 0;
    }
};