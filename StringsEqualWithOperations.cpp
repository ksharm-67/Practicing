class Solution {
public:
    bool canBeEqual(string s1, string s2) {
        
        //do s1
        for(int i = 0; i < 2; i++){
            if(s1 == s2) return true;
            
            else{
                swap(s1[i], s1[i + 2]);
                if(s1 == s2) return true;
            }
        }


        for(int i = 0; i < 2; i++){
            if(s1 == s2) return true;
            
            else{
                swap(s2[i], s2[i + 2]);
                if(s1 == s2) return true;
            }
        }

        return false;
    }
};
