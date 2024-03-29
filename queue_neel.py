                                                    # queue using linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue_linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def enqueue(self,data):
        current=self.head
        newNode=Node(data)
        # 8,9,6,3,2,7
        # head=8
        # newNode=7
        if self.size==0:
            self.head=newNode
            # print("this is the list ")
        else:
            # while current.next is not None:
            #     current = current.next
            self.tail.next = newNode
        self.tail=newNode
        self.size += 1

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end='->')
            current = current.next
        print("None")

    def deququq(self):
        if self.is_empty():
            print("the list is empty")
            return
        self.head=self.head.next
        self.size -= 1

    def is_empty(self):
        if self.size==0:
            return True
        else:
            return False

x=Queue_linked_list()
x.deququq()
x.enqueue(8)
x.enqueue(7)
x.enqueue(6)
x.enqueue(5)
x.enqueue(3)
x.enqueue(4)
x.display()
(x.deququq())
x.deququq()
x.deququq()
x.display()