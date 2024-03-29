
                                   #stack implementation using linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None
        self.size=0

    def push(self,data):
        newNode=Node(data) #inside box element
        newNode.next=self.head
        self.head=newNode
        self.size += 1
    #   8,3,6,4
    #

    def display(self):
        current=self.head
        # 8->5->6->7->9->None
        # current=8,5,6,7,9
        #
        while current.next is not None:
            print(current.data,end='->')
            current=current.next
        print("None")

    def pop(self):
        if self.is_empty():
            print("the list is empty")
            return
        # 8,3,6,4
        # head=8
        # head.next=
        num=self.head.data
        self.head=self.head.next
        # head=3
        self.size -= 1
        return num

    def is_empty(self):
        if self.size==0:
            return True
        else:
            return False

    def peek(self):
        print(self.head.data)

x=Linked_list()
x.push(1)
x.push(2)
x.push(3)
x.push(4)
x.push(5)
x.push(6)
x.pop()
x.peek()
# x.pop()
# x.pop()
# x.pop()
# x.pop()
# x.pop()
x.display()