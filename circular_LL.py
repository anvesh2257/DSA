class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        # self.head=None
        self.tail=None
        self.size=0


    def insert_head(self,data):
        newNode=Node(data)
        if self.is_empty():
            self.tail=newNode
        # 8,9,5,4,6
        #head=8
        newNode.next=self.tail.next #inserting new node before the current head since we are insert head function
        self.tail.next=newNode #assigning new node as head
        self.size += 1

    def insert_tail(self,data):
        newNode=Node(data)
        if self.is_empty():
            self.tail.next=newNode
            self.tail=newNode
            self.size += 1
            return
        # current=self.tail.next
        # while current.next is not None:  #search for the tail node
        #     current=current.next
        newNode.next = self.tail.next
        self.tail.next=newNode
        # newNode.next=self.tail.next
        self.tail = newNode
        self.size += 1


    def delete_head(self):
        if self.is_empty():
            print("the list is empty")
            return
        self.tail.next=self.tail.next.next
        self.size -= 1


    def delete_tail(self):
        if self.is_empty():
            print("the list is empty")
            return
        current=self.tail.next
        while current.next is not self.tail:
            current=current.next
            # print(current.data)
        current.next=self.tail.next
        self.tail=current
        self.size -= 1


    def display(self):
        current=self.tail.next
        # print(self.tail.data)
        while current is not self.tail:
            print(current.data,end='->')
            current=current.next
        print(self.tail.data)

    def is_empty(self):
        return self.size==0

x=Linked_list()
x.insert_head(4)
x.insert_head(3)
x.display()
x.insert_tail(5)
x.display()
x.delete_tail()
x.display()
x.delete_head()
x.display()
