import myModule as m
stack_size=int(input("Ente the size of the stack"))
stack=[]

for i in range(stack_size):
    value=int(input("Enter a value to push in the stack"))
    m.push(stack,value,stack_size)
search_element=input("Enter the element to search in the stack")
if search_element in stack:
    print(f"{search_element} is present in the stack")
else:
    print(f"{search_element} is not present in the stack")

for i in range(5):
    m.pop(stack)

m.display(stack)