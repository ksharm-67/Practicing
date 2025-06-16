    #include <iostream>
    #include <vector>

    using namespace std;
    
    vector<int> sortArrayByParity(vector<int>& nums) {
        
        if (nums.size() == 1) return {nums};

        vector<int> even;
        vector<int> odd;

        for(int i = 0; i < nums.size(); i++){
            if(nums[i] % 2 == 0) even.push_back(nums[i]);
            else odd.push_back(nums[i]);
        }

        for(int j = 0; j < odd.size(); j++){
            even.push_back(odd[j]);
        }

        return even;
    }