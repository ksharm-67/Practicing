#include <iostream>
#include <vector>

using namespace std;

struct Node{
    int data;
    Node* left;
    Node* right;
};

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

    root = insert(root, 4);
    root = insert(root, 1);
    root = insert(root, 9);
    root = insert(root, 3);
    root = insert(root, 6);
    
    cout << "Is 8 present? 1 if true, 0 if not: " << search(root, 8) << endl;
    cout << "Is 6 present? 1 if true, 0 if not: " << search(root, 6) << endl;
    cout << "Is 1 present? 1 if true, 0 if not: " << search(root, 1) << endl;

    return 1;
}