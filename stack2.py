#Stack implementation using class and methods

class Stack:
    def __init__(self):
        self.stack=[]

    def isEmpty(self): #method to check stack is empty or not
        isempty = not bool(self.stack)
        #return len(self.stack)==0
        return isempty

    def push(self,element):# method for pushing or inserting elements in the stack
        self.stack.append(element)

    def pop(self): # method for poping or removing elements in the stack
        if self.isEmpty():
            return "Stack is Already empty"
        self.stack.pop()

    def length(self): # method to check the length of the stack
        return len(self.stack)

    def printStack(self): # method to print the stack
        print("Current stack's elements are: ",self.stack)



mystack = Stack()
print('\n')
print("Stack after initilizing without eny element\n")
mystack.printStack()
print("Stack's current length: ", mystack.length())
print("Is Stack Empty: ", mystack.isEmpty())
print('\n')
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)
mystack.push(5)

print("Stack after pushing elements")
mystack.printStack()
print("Stack's current length: ", mystack.length())
print("Is Stack Empty: ", mystack.isEmpty())
print('\n')



mystack.pop()
print("Stack after poping an element")
mystack.printStack()
print("Stack's current length: ", mystack.length())

print('\n')
mystack.pop()
print("Stack after poping again element")
mystack.printStack()
print("Stack's current length: ", mystack.length())
print("Is Stack Empty: ", mystack.isEmpty())

