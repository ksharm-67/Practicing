#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Node{
    int data;
    Node* left;
    Node* right;
};

int findHeight(Node* root){
    
    if(root == nullptr) return -1;

    return max(findHeight(root->left), findHeight(root->right)) + 1;
}

Node* insert(Node* root, int data){

    if (root == nullptr) {
        Node* temp = new Node();
        temp->data = data;
        temp->left = nullptr;
        temp->right = nullptr;
        return temp;
    }

    else if(data < root->data){
        root->left = insert(root->left, data);
    }

    else{
        root->right = insert(root->right, data);
    }
    return root;
}

int findMin(Node* root){
    
    Node* temp = root;

    if(temp == nullptr) {
        cout << "error, empty"; 
        return -1;
    }

    while(temp->left != nullptr) temp = temp->left;

    return temp->data;
}

int findMax(Node* root){
    
    Node* temp = root;

    if(temp == nullptr) {
        cout << "error, empty"; 
        return -1;
    }

    while(temp->right != nullptr) temp = temp->right;

    return temp->data;
}

bool search(Node* root, int data){
    
    if(root == nullptr) return false;
    else if(data == root->data) return true;
    else if(data <= root->data) return search(root->left, data);
    else return search(root->right, data);

}

int main(){

    Node* root = new Node();
    root->data = 10;
    root->left = nullptr;
    root->right = nullptr;

    vector<int> values = {5, 2, 8, 1, 3, 6, 9, 4, 7};
    for (int val : values) {
        root = insert(root, val);
    }


    cout << "Is 14 present? 1 if true, 0 if not: " << search(root, 14) << endl;
    cout << "Is 6 present? 1 if true, 0 if not: " << search(root, 6) << endl;
    cout << "Is 1 present? 1 if true, 0 if not: " << search(root, 1) << endl;

    cout << "Minimum element: " << findMin(root) << endl;
    cout << "Maximum element: " << findMax(root) << endl;
    cout << "Height of the Tree: " << findHeight(root) << endl;

    return 1;
}