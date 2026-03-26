class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node5.prev = node4
node4.prev = node3
node3.prev = node2
node2.prev = node1



print("node1's data =", node1.data," Address of the next node, node2's address = ", node1.next)
print("node2's data =", node2.data," Address of the next node, node3's address = ", node2.next)
print("node3's data =", node3.data," Address of the next node, node4's address = ", node3.next)
print("node4's data =", node4.data," Address of the next node, node5's address = ", node4.next)
print("node5's data =", node5.data," Address of the next node, node n's address = ", node5.next)

print("node5's data =", node5.data," Address of the prev node, node n's address = ", node5.prev)
print("node4's data =", node4.data," Address of the prev node, node5's address = ", node4.prev)
print("node3's data =", node3.data," Address of the prev node, node4's address = ", node3.prev)
print("node2's data =", node2.data," Address of the prev node, node3's address = ", node2.prev)
print("node1's data =", node1.data," Address of the prev node, node2's address = ", node1.prev)


head = node1

print("\n Here the Doubly linked list's forward traversal will look like something as per our assumption \n")

while head != None:
    print(head.data, "->", end = " ")
    head = head.next
print("None")    


print("\n Here the Doubly linked list's backward traversal will look like something as per our assumption \n")

head = node5

while head != None:
    print(head.data, "->", end = " ")
    head = head.prev
print("None")    