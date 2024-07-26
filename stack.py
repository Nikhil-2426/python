stack=[]

stack.append('M')
stack.append('N')
stack.append('O')
print("Intial stack is:")
print(stack)

print("\nElemnets popped from stack")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("Elements after popping")
print(stack)


print("Queue")

from queue import LifoQueue

qu=LifoQueue(maxsize=3)
print("Intial size: ",qu.qsize())
qu.put("M")
qu.put("N")
qu.put("O")

print("Full: ",qu.full())
print("Size: ",qu.qsize())

print(qu.get())
print(qu.get())
print(qu.get())


print("Empty",qu.empty())
print("\n")

queue=[]

queue.append('M')
queue.append('N')
queue.append('O')
print("Intial queue is:")
print(queue)

print("\nElemnets popped from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("Queue after popping")
print(queue)
print("\n")

from queue import Queue

q=Queue(maxsize=3)
print("Inital size",q.qsize())

q.put("M")
q.put("N")
q.put("O")

print("Full: ",q.full())

print(q.get())
print(q.get())
print(q.get())

print("Empty",q.empty())
q.put(1)
print("Full: ",q.full())
print("Empty:",q.empty())

from collections import deque

qu=deque()
qu.append('H')
qu.append('G')
qu.append('A')
print("Initial queue")
print(qu)


print(qu.popleft())
print(qu.popleft())
print(qu.popleft())
print("Elements after popping")
print(qu)










