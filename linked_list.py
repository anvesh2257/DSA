#create nodes
#created linked list
#add nodes to ll
#print ll

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=none
#
# class linkedList:
#     def __init__(self):
#         self.head(none)
#
#     def insert(self,newNode):
#         if self.head is None:
#             self.head=newNode
#         else:
#             lastNode=self.head
#             while True:
#                 if lastNode.next is None:
#                     break
#                 lastNode=lastNode.next
#             lastNode.next=newNode
#
#     def printList(self):
#         if self.head is None:
#             print("List is empty")
#             return
#         currentNode=self.head
#         while True:
#             if currentNode is None:
#                 break
#             print(currentNode.data)
#             currentNode=currentNode.next
#
# firstNode=Node("Jhon")
# linkedList=linkedList()
# LinkedList.insert(firstNode)
# secondNode=Node("ben")
# LinkedList.insert(secondNode)
# thirdNode=Node("mathew")
# linkedList.insert(thirdNode)
# linkedList.printList()

                     #head Node insertion
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# class linkedList:
#     def __init__(self):
#         self.head=None
#
#     def insertHead(self,newNode):
#         temporaryNode=self.head
#         self.head=newNode
#         self.head.next=temporaryNode
#         del temporaryNode
#
#     def insertEnd(selfself,newNode):
#         if self.head is None:
#             self.head=newNode
#         else:
#             lastNode=self.head
#             while True:
#                 if lastNode.next is None:
#                     break
#                 lastNode=lastNode,next
#             lastNode.next=newNode
#
#     def printList(self):
#         if self.head is None:
#             print("list is empty")
#             return
#         currentNode=self.head
#         while True:
#             if currentNode is None:
#                 break
#             print(currentNode.data)
#             currentNode=currentNode.next
#
# firstNode=Node("Jhon")
# linkedList=linkedList()
# linkedList.insertEnd(firstNode)
# secondNode=Node("ben")
# linkedList.insertEnd(secondNode)
# thirdNode=Node("mathew")
# linkedList.insertHead(thirdNode)
# linkedList.printList()

class Browser:
    def __init__(self):
        self.history = []  # Stack to store the visited pages
        self.forward_stack = []  # Stack to store forward pages

    def visit_page(self, page):
        self.history.append(page)  # Add the page to history
        # Limit history to 10 pages
        if len(self.history) > 10:
            self.history = self.history[-10:]

        # Clear forward stack since we are visiting a new page
        self.forward_stack = []

    def go_back(self):
        if len(self.history) > 1:
            # Pop the current page from history and push it to the forward stack
            current_page = self.history.pop()
            self.forward_stack.append(current_page)
            # Get the previous page
            previous_page = self.history[-1]
            return previous_page
        else:
            print("No more pages to go back to.")
            return None

    def go_forward(self):
        if self.forward_stack:
            # Pop the top page from the forward stack
            next_page = self.forward_stack.pop()
            # Add the next page to the history
            self.history.append(next_page)
            return next_page
        else:
            print("No forward history.")
            return None


def main():
    browser = Browser()

    while True:
        print("\n1. Visit Page")
        print("2. Go Back")
        print("3. Go Forward")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            page = input("Enter the URL of the page: ")
            browser.visit_page(page)
            print(f"You visited {page}")

        elif choice == '2':
            page = browser.go_back()
            if page:
                print(f"Going back to {page}")

        elif choice == '3':
            page = browser.go_forward()
            if page:
                print(f"Going forward to {page}")

        elif choice == '4':
            print("Exiting the browser.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
