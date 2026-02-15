class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        isempty = not bool(self.queue)
        return isempty

    def enqueue(self,element):
        self.queue.append(element)

    def dequeue(self):
        self.queue.pop(0)

    def prints(self):
        print("Current element of the Queue", self.queue)

    def length(self):
        print("Current length of the queue =", len(self.queue))    

myqueue = Queue()

print("\nQueue before inserting any elements\n")
myqueue.prints() # prints the current status of the queue
myqueue.isEmpty() # checks that the current queue is empty or not
myqueue.length() # checks the length of the queue

myqueue.enqueue(1) # inserting the first element of the queue
myqueue.enqueue(2)
myqueue.enqueue(3)
myqueue.enqueue(4)
myqueue.enqueue(5)

print("\nQueue after entering/enqueuing the elements\n")    
myqueue.prints() 
myqueue.isEmpty() 
myqueue.length() 


myqueue.dequeue() # deleting the element of the queue or dequeueing, FIFO(first-in-first- out)
myqueue.dequeue()
myqueue.dequeue()

print("\nAfter removing or dequeueing few elements from the queue\n")
myqueue.prints() 
myqueue.isEmpty() 
myqueue.length() 