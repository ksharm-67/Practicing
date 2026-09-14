class Solution {
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        // first rectangle
        int ax1 = rec1[0], ay1 = rec1[1];                    // bottom left
        int ax2 = rec1[2], ay2 = rec1[3];                    // top right
        // second rectangle 
        int bx1 = rec2[0], by1 = rec2[1];
        int bx2 = rec2[2], by2 = rec2[3];

        int ax3 = ax1, ay3 = ay2, ax4 = ax2, ay4 = ay1;     // top left, bottom right
        int bx3 = bx1, by3 = by2, bx4 = bx2, by4 = by1;     

        if(bx1 >= ax2 || by1 >= ay2 || ax1 >= bx2 || ay1 >= by2) return false;
        return true;
        
    }
};
