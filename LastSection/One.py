class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, value):
        if not self.isfull():
            self.stack.append(value)
            print(f"Pushed {value} onto the stack")
        else:
            print("Stack is full. Cannot push more elements.")

    def pop(self):
        if not self.isempty():
            return self.stack.pop()
        else:
            print("Stack is empty. Cannot pop elements.")
            return None

    def isempty(self):
        return len(self.stack) == 0

    def isfull(self):
        return len(self.stack) == self.size

    def peak(self):
        if not self.isempty():
            return self.stack[-1]
        else:
            print("Stack is empty. Cannot peek.")
            return None


class CustomStack(Stack):
    def __init__(self, size):
        super().__init__(size)

    def delete_elements(self, num):
        if len(self.stack) >= num:
            for _ in range(num):
                self.pop()
            print(f"Deleted {num} elements from the stack")
        else:
            print("Stack does not have enough elements to delete.")

    def display_stack(self):
        if not self.isempty():
            print("Elements in the stack:")
            for element in self.stack:
                print(element)
        else:
            print("Stack is empty.")


# Main program
stack_size = 20
user_values = [int(input(f"Enter value {i + 1}: ")) for i in range(stack_size)]

custom_stack = CustomStack(stack_size)

# Inserting values into the stack
for value in user_values:
    custom_stack.push(value)

# Searching for an element in the stack
search_element = int(input("Enter element to search: "))
if search_element in custom_stack.stack:
    print(f"{search_element} found in the stack")
else:
    print(f"{search_element} not found in the stack")

# Deleting 5 elements from the stack
custom_stack.delete_elements(5)

# Displaying remaining elements in the stack
custom_stack.display_stack()

