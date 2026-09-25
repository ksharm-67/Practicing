class Node:
    def __init__(self, val, idx):
        self.val = val
        self.next = None
        self.idx = idx

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.top = None

    def get(self, index: int) -> int:
        temp = self.head
        while temp:
            if temp.idx == index:
                return temp.val
            temp = temp.next
            
        return -1        

    def addAtHead(self, val: int) -> None:
        newHead = Node(val, 0)
        if not self.head:
            self.head = newHead
            self.top = newHead

        else:
            x = self.head
            self.head = newHead
            newHead.next = x

            temp = self.head.next
            while temp:
                temp.idx += 1
                temp = temp.next

    def addAtTail(self, val: int) -> None:
        newNode = Node(val, 0)
        if not self.head:
            self.head = newNode

        elif not self.head.next:
            self.head.next = newNode
            newNode.idx = 1

        else:
            self.top.next = newNode
            newNode.idx = self.top.idx + 1

        self.top = newNode                

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        
        if not self.head:
            return

        if index == self.top.idx + 1:
            newNode = Node(val, self.top.idx + 1)
            self.top.next = newNode
            self.top = newNode
            return

        temp = self.head
        while temp:
            if temp.idx == index - 1:
                newNode = Node(val, index)
                
                nextNode = temp.next
                temp.next = newNode
                newNode.next = nextNode

                break
            temp = temp.next
        
        if temp:
            temp = newNode.next
            while temp:
                temp.idx += 1
                temp = temp.next
        return 

    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        if not self.head or index > self.top.idx:
            return

        if index == 0 and not self.head.next:
            self.head = None
            self.top = None
            return

        if index == 0:
            self.head = self.head.next
            temp = self.head
            while temp:
                temp.idx -= 1
                temp = temp.next
            return

        while temp:
            if temp.idx == index - 1:
                if self.top.idx == index:
                    self.top = temp
                    self.top.next = None
                else:
                    temp.next = temp.next.next
                break
            temp = temp.next
        
        temp = temp.next
        while temp:
            temp.idx -= 1
            temp = temp.next
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
