class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def insert_head(self,data):
        newNode=Node(data)
        # 8,9,5,4,6
        #head=8
        newNode.next=self.head  #inserting new node before the current head since we are insert head function
        self.head=newNode #assigning new node as head
        self.size += 1

    def insert_tail(self,data):
        newNode=Node(data)
        if self.is_empty():
            self.head=newNode
            self.size += 1
            return
        current=self.head
        # print("before while current=",current.data)
        while current.next is not None:  #search for the tail node
            current=current.next
            # print("current=",current.data)
        # print("after while current=",current.data)
        current.next=newNode
        # print("newnode=",newNode.data)
        self.size += 1


    def delete_head(self):
        if self.is_empty():
            print("the list is empty")
            return
        self.head=self.head.next
        self.size -= 1


    def delete_tail(self):
        if self.is_empty():
            print("the list is empty")
            return
        current=self.head
        while current.next.next is not None:
            current=current.next
            # print(current.data)
        current.next=None
        self.size -= 1


    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end='->')
            current=current.next
        print("none")


    def is_empty(self):
        return self.size==0

# print("stack")
# stack=Linked_list()
# stack.insert_head(3)
# stack.insert_head(2)
# stack.insert_head(1)
# stack.insert_tail(4)
# stack.display()
# stack.delete_head()
# stack.display()
print("queue")
queue=Linked_list()
queue.insert_tail(5)
queue.insert_tail(4)
queue.insert_tail(6)
queue.insert_tail(3)
queue.insert_tail(2)
queue.insert_tail(1)
queue.display()
queue.delete_head()
queue.display()
queue.delete_tail()
queue.delete_tail()
queue.display()
