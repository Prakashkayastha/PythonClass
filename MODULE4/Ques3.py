import myModule as m
queue_size=int(input("Enter the size of the queue"))
queue=[]

for i in range(queue_size):
    value=int(input("Enter the element:"))
    m.insert(queue,value,queue_size)

search_element=int(input("Enter the element to search in the queue:"))

if search_element in queue:
    print(f"{search_element} is present in the queue")
else:
    print(f"{search_element} is not present in the queue")

for i in range(5):
    m.delete(queue)

m.display(queue)