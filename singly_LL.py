class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("node1's data =", node1.data," Address of the next node, node2's address = ", node1.next)
print("node2's data =", node2.data," Address of the next node, node3's address = ", node2.next)
print("node3's data =", node3.data," Address of the next node, node4's address = ", node3.next)
print("node4's data =", node4.data," Address of the next node, node5's address = ", node4.next)
print("node5's data =", node5.data," Address of the next node, node n's address = ", node5.next)

head = node1

print("\n Here the singly linked list will look like something as per our assumption \n")

while head != None:
    print(head.data, "->", end = " ")
    head = head.next
print("None")    
