class Solution {
public:
    int maximum69Number(int num) {
        if(num == 6) return 9;
        if(num == 9) return 9;

        vector<int> changed;
        changed.push_back(num);

        string temp = to_string(num);
        for(int i = 0; i < temp.size(); i++){
            if(temp[i] == '6') temp[i] = '9';
            else continue;
            changed.push_back(stoi(temp));
            temp = to_string(num);
        }

        int max = changed[0];
        for(auto c : changed) {
            if(c > max) max = c;
        }

        return max;
    }
};