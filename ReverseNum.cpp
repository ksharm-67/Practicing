#include <iostream>
#include <string>

//Function to reverse a number (eg. 1034 becomes 4301)
int reverse(int x) {
        string y = to_string(x);
        y.erase(remove(y.begin(), y.end(), '-'), y.end());
        string z = "";

        for(int i = y.size() - 1; i >= 0; i--){
            cout << y[i];
            z += y[i];
        }

        try{
            if(x < 0) return -stoi(z);
            else return stoi(z);
        }
        catch(const out_of_range& e){
            return 0;
        }
  }
