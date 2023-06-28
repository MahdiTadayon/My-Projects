
stack = list() # Creating a stack

def pushToStack(anything): # Inserting an element into the stack.(last in)
    stack.append(anything)


def popFromStack(): # Remove the topmost element from the stack.(first out)
    if not isEmpty():
        stack.pop()


def isEmpty(): # Check whether the stack is empty or not.
    if len(stack) == 0:
        return True


def peek(): # Get top most element.
    return stack[-1]


def displayStack(): # Displaying the stack elements.
    for index, value in enumerate(stack):
        print('Push element {} : {}'.format(index, value))
    if isEmpty:
        print('The stack is empty')

    print("--------------------")

if __name__ == "__main__":

    displayStack()

    pushToStack('Mahdi Tadyon')
    pushToStack(1999)
    displayStack()
    popFromStack()
    displayStack()
    popFromStack()
    popFromStack()
    pushToStack('python')
    pushToStack(3)
    popFromStack()
    displayStack()




