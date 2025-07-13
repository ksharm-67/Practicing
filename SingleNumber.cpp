class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int, int> mp;

        if (nums.size() == 1) return nums[0];

        for(int i = 0; i < nums.size(); i++){
            
            auto itr = mp.find(nums[i]);

            if(itr != mp.end()){
                mp[nums[i]] += 1;
            }
            else mp[nums[i]] = 1;

        }

        for(auto m : mp){
            cout << m.first << " : " << m.second << endl;
            if (m.second == 1) return m.first;
        }

        return 0;
    }
};
