class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        
        vector<int> positive, negative;
        
        for(int num : nums) {
            if(num >= 0) positive.push_back(num);
            else negative.push_back(num);
        }
        
        vector<int> res(nums.size());
        
        for(int i = 0; i < nums.size() / 2; i++) {
            res[2*i] = positive[i];
            res[2*i + 1] = negative[i];
        }
        
        return res;
    }
};