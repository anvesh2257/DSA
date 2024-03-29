class Queue:
    def __init__(self):
        self.qlist=[]

    def enqueue(self,data):
        self.qlist.append(data)

    def dequeue(self):
        if self.is_empty():
            print("list is empty")
            return
        self.qlist.pop(0)

    def display(self):
        print(self.qlist)

    def is_empty(self):
        return self.qlist==[]

x=Queue()
x.enqueue(5)
x.enqueue(4)
x.enqueue(3)
x.enqueue(2)
x.enqueue(1)
x.display()
x.dequeue()
x.dequeue()
x.dequeue()
x.dequeue()
x.dequeue()
x.dequeue()
x.display()
