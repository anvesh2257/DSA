class DoublyLinkedBase:
    class Node:
        __slots__ = 'element', 'prev', 'next'

        def __init__(self, element, prev=None, next=None):
            self.element = element
            self.prev = prev
            self.next = next

    def __init__(self):
        self.header = self.Node(None)
        self.trailer = self.Node(None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_between(self, e, predecessor, successor):
        new_node = self.Node(e, predecessor, successor)
        predecessor.next = new_node
        successor.prev = new_node
        self.size += 1
        return new_node

    def delete_node(self, node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        element = node.element
        node.prev = node.next = node.element = None
        return element


dll = DoublyLinkedBase()


print("Is empty?: ", dll.is_empty())
node1 = dll.insert_between(1, dll.header, dll.trailer)
node2 = dll.insert_between(2, node1, dll.trailer)
node3 = dll.insert_between(3, node1, node2)
node4 = dll.insert_between(8, dll.header, node1)

print("Original List:")
current_node = dll.header.next
while current_node != dll.trailer:
    print(current_node.element,end="->")
    current_node = current_node.next

deleted_element = dll.delete_node(node1)
print("\nDeleted Element:", deleted_element)

print("\nList after Deletion:")
current_node = dll.header.next
while current_node != dll.trailer:
    print(current_node.element,end="->")
    current_node = current_node.next

print("Is empty?: ", dll.is_empty())