#include <iostream>
#include <stack>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        if (s.empty()) return true;
        st.push(s[0]);

        for (int i = 1; i < s.size(); i++) {
            if (!st.empty() &&
                ((s[i] == ')' && st.top() == '(') ||
                 (s[i] == '}' && st.top() == '{') ||
                 (s[i] == ']' && st.top() == '['))) {
                st.pop();
            } else {
                st.push(s[i]);
            }
        }

        return st.empty();
    }
};
