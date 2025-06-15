#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

//Function to group anagrams from a vector like [tab, art, cat, bat, tar] and return them [[art, tar],[bat,tab],[cat]] together
vector<vector<string>> GroupAnagrams(vector<string> an){

    vector<vector<string>> res;
    unordered_map<string, vector<string>> mp;

    for(int i = 0; i < an.size(); i++){
        string temp = an[i];

        sort(temp.begin(), temp.end());
        
        mp[temp].push_back(an[i]);
    }

    for(auto m : mp){
        res.push_back(m.second);
    }

    return res;
}

int main(){

    //Enter your vector here
    vector<vector<string>> ga = GroupAnagrams({"tab", "art", "cat", "bat", "tar"});

    for(int i = 0; i < ga.size(); i++){
        cout << "[ ";
        for(const auto& c : ga[i]){
            cout << c << " ";
        }
        cout << "]" << endl;
    }
}