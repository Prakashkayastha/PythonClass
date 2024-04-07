def isFull(stack,stack_size):
    return len(stack) == stack_size


def isempty(stack):
    return len(stack) == 0

def push(stack,element,stack_size):
    if  not isFull(stack,stack_size):
        stack.append(element)
    else:
        print("Stack is full,cannot push element")


def pop(stack):
    if not isempty(stack):
        return stack.pop()
    else:
        print("Stack is empty,cannot pop element")
        return None


def peak(stack):
    if not isempty(stack):
        return stack[-1]
    else:
        print("Stack is empty,cannot peak element")
        return None


def display(stack):
    if not isempty(stack):
        print("Element are in the stack:")
        for element in reversed(stack):
            print(element)
    else:
        print("Stack is empty")