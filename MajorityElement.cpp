class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int maj;

        unordered_map<int, int> mp;

        for(int i = 0; i < nums.size(); i++){

            auto itr = mp.find(nums[i]);

            if(itr != mp.end()){
                mp[nums[i]]++;
            }
            else{
                mp[nums[i]] = 1;
            }
        }

        for(auto m : mp){
            cout << m.first << " : " << m.second << endl;
            if(m.second > floor(nums.size() / 2)) return m.first;
        }

        return 0;
    }
};