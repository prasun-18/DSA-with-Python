# Simple Stack implementation

stack =[] #initializing a empty stack
print("Stack before pushing any element",stack)

#push: To inster the data in the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

print("Stack after pushing any element",stack)

#pop: To delete the data in the stack
stack.pop()

print("Stack after poping an element",stack)

stack.pop()
print("Stack after poping 2nd time in a row",stack)


# isEmpty : to check that our stack is emoty or not
isEmpty = not bool(stack)
print("Stack is Empyt: ",isEmpty)


#len : to check the length of the stack
length = len(stack)
print("The length of the stack: ",length)