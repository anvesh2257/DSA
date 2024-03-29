# def push(a):
#     list1.append(a)
#
# def pop():
#     if is_empty():
#         print("list is empty")
#     else:
#         list1.pop()
#
#
# def display():
#     if is_empty():
#         print("list is empty")
#         print(list1)
#     else:
#         print(list1)
#
# def is_empty():
#     if list1==[]:
#         return True
#     else:
#         return False
#
#
#
# list1=[1,2,3,4]
# push(25)
# push(36)
# # push(10,25,35,45)
# display()
# pop()
# display()
# x=is_empty()
# print(x)
# pop()
# pop()
# pop()
# pop()
# pop()
# display()
# print(is_empty()
class stack():
    def __init__(self):
        self.stk_list=[]

    def push(self,a):
        self.stk_list.append(a)
        print(self.stk_list)


    def pop(self):
        if self.is_empty():
            print("list is empty")
        else:
            self.stk_list.pop()
            print(self.stk_list)

    def is_empty(self):
        if self.stk_list==[]:
            return True
        else:
            return False


x=stack()
x.push(2)
x.push(3)
x.push(4)
x.push(5)
x.is_empty()
x.pop()
x.pop()
x.pop()
x.pop()
x.is_empty()
x.pop()





