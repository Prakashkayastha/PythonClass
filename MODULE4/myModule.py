def isempty(queue):
   return len(queue) == 0


def isFull(queue,queue_size):
   return len(queue) == queue_size

def insert(queue,element,queue_size):
   if not isFull(queue,queue_size):
      queue.append(element)
   else:
      print("queue is full,cannot push element")

def delete(queue):
   if not isempty(queue):
      return queue.pop(0)
   else:
      print("Queue is empty,cannot peak element")

def display(queue):
   if not isempty(queue):
      print("Element in the queue")
      for element in queue:
         print(element)
   else:
      print("Queue is empty")
