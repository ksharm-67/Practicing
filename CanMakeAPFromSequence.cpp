class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        if(arr.size() == 2) return true;
        sort(arr.begin(), arr.end());

        //for(auto& a : arr) cout << a << ", ";

        int firstDiff = arr[1] - arr[0];
        for(int i = 2; i < arr.size(); i++){
            if(arr[i] - arr[i - 1] != firstDiff) return false;
        }
        
        return true;
    }
};
