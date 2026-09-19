class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        long long res = 0, curr = 0;

        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == 0) curr++;
            else curr = 0;
            res += curr;
        }
        
        return res;
    }
};
