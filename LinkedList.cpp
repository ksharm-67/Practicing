#include <iostream>

using namespace std;

struct Node {
    int data;
    Node* next;
};

//Remove a node from the end of a LinkedList
void removeNode(Node* head){
    Node* temp = head;

    Node* prev = nullptr;

    //Return this if there's only one element (can't delete it)
    if(temp->next == nullptr) return;

    while(temp->next != nullptr){
        prev = temp;
        temp = temp->next;
    }
    //temp is the last element, and prev is second last when this loop ends

    //We also want to set temp's address to nullptr, not just delete it
    prev->next = nullptr;
    delete temp;
}

//Remove a node from the head of a LinkedList and return the new head
Node* removeHead(Node* head){

    if(head->next == nullptr) return head;      //Do not remove the head, as there is only one element

    Node* prev = head;
    head = head->next;
    delete prev;
    return head;
}

//Create a node and insert at the end of a LinkedList and set its value
Node* createNode(Node* head, int val){

    Node* newNode = new Node();
    newNode->data = val;
    newNode->next = nullptr;

    //If the list is empty
    if(head == nullptr) {return newNode;}

    //If the list isn't empty
    Node* temp = head;
    while(temp->next != nullptr){
        temp = temp->next;
    }

    temp->next = newNode;
    newNode->next = nullptr;
    return head;
}

//Reverse the LinkedList and return a pointer to head
Node* reverseList(Node* head){
    Node* currentNode = head;
    Node* prevNode = nullptr;

    //Return the head if it's the only element in the LinkedList
    if (head == nullptr || head->next == nullptr) return head;

    while(currentNode != nullptr){
        Node* nextNode = currentNode->next;
        currentNode->next = prevNode;
        prevNode = currentNode;
        currentNode = nextNode;
    }

    head = prevNode;
    return head;
}

//Traverse through the LinkedList
void printList(Node* head){
    Node* temp = head;

    while(temp != nullptr){
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

int main(){
    Node* head = nullptr;

    head = createNode(head, 41);
    head = createNode(head, 84);
    head = createNode(head, 97);
    head = createNode(head, 66);

    head = reverseList(head);

    printList(head);
}