class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> max_left(n), min_right(n);
        max_left[0] = nums[0];
        min_right[n - 1] = nums[n - 1];

        for(int i = 1; i < n; i++) max_left[i] = max(max_left[i - 1], nums[i]);
        for(int i = n - 2; i >= 0; i--) min_right[i] = min(min_right[i + 1], nums[i]);

        for(int i = 0; i < n; i ++) if(max_left[i] - min_right[i] <= k) return i;
        return -1;
    }
};
