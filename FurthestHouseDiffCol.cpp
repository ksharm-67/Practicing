class Solution {
public:
    int maxDistance(vector<int>& colors) {
        int distL = 0, left = 0, right = colors.size() - 1;
        
        while(left < right){
            if(colors[left] == colors[right]) left++;
            else{
                distL = max(distL, abs(right - left));
                left++;
            }
        }

        int distR = 0;
        left = 0, right = colors.size() - 1;

        while(left < right){
            if(colors[left] == colors[right]) right--;
            else{
                distR = max(distR, abs(right - left));
                right--;
            }
        }
    
        return max(distL, distR);
    }
};
