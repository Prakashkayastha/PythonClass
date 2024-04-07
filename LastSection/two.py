class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size

    def insert(self, value):
        if not self.is_full():
            self.queue.append(value)
            print(f"Inserted {value} into the queue")
        else:
            print("Queue is full. Cannot insert element.")

    def delete(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty. Cannot delete element.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty. Cannot peek.")
            return None

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty. Cannot peek.")
            return None

class QueueWithStack(Queue, Stack):
    def __init__(self, size):
        Queue.__init__(self, size)
        Stack.__init__(self)

    def display_remaining_elements(self):
        print("Remaining elements in the queue:")
        for element in self.queue:
            print(element)

# Create a queue with size 20
queue = QueueWithStack(20)

# Insert 20 user-defined values into the queue
for i in range(20):
    queue.insert(input(f"Enter element {i+1}: "))

# Search for a user-defined element using peak operation of stack
search_element = input("Enter the element to search: ")
if search_element in queue.stack:
    print(f"{search_element} is found in the queue.")
else:
    print(f"{search_element} is not found in the queue.")

# Delete 5 elements from the queue
print("Deleted elements from the queue:")
for _ in range(5):
    deleted_element = queue.delete()
    if deleted_element:
        print(deleted_element)

# Display all remaining elements of the queue
queue.display_remaining_elements()
