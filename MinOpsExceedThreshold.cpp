class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        
        int res = 0;
        sort(nums.begin(), nums.end());
        
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] >= k) return res;
            else res++;
        }

        return res;
    }
};