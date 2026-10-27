class Solution {
public:
    int smallestBalancedIndex(vector<int>& nums) {
        long long sum = accumulate(nums.begin(), nums.end(), 0LL);
        long long prod = 1LL;

        for(int i = nums.size() - 1; i > 0; i--) {
            sum -= nums[i];
            if(sum == prod) return i;
            if (sum < prod) break;
            if (nums[i] != 0 && prod > sum / nums[i]) break;
            
            prod *= nums[i];
        }

        return -1;
    }
};
