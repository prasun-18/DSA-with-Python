
#Initializing the Queue
queue = []

print("Queue before appending: ", queue)

# IsEmpty
IsEmpty = not bool(queue)
print("IsEmpty", IsEmpty)

# Enqueue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

print("Queue after inserting the element: ", queue)


# IsEmpty
IsEmpty = not bool(queue)
print("IsEmpty", IsEmpty)

# Dequeue
queue.pop(0)
print("Queue after removing element:", queue)
queue.pop(0)
print("Queue after removing element:", queue)
queue.pop(0)
print("Queue after removing element:", queue)

# IsEmpty
IsEmpty = not bool(queue)
print("IsEmpty", IsEmpty)