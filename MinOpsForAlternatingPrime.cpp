class Solution {
public:
    bool isPrime(int num){
        if(num < 2) return false;
        for(int i = 2; i * i <= num; i++){
            if(num % i == 0) return false;
        }
        return true;
    }

    int nearestPrime(int num){
        num++;
        while(true){
            if(isPrime(num)) return num;
            num++;
        }
        return num;
    }

    int minOperations(vector<int>& nums) {
        int res = 0;
        for(int i = 0; i < nums.size(); i++){
            // should be prime
            if(i % 2 == 0){
                if(!isPrime(nums[i])) res += nearestPrime(nums[i]) - nums[i];
            }

            // shouldn't be prime
            else{
                if(isPrime(nums[i])) {
                    if(nums[i] > 2) res += 1;
                    else res += 2;
                }
            }
        }
        return res;
    }
};
