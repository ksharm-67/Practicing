class Solution {
public:
    int minAddToMakeValid(string s) {
        int open = 0, closed = 0;
        for(auto& c : s) {
            if(c == ')' && open == 0) closed += 1;
            else if(c == '(') open += 1;
            else open -= 1;
        }
        
        return open + closed;
    }
};
