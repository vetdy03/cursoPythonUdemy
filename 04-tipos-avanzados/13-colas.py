#FIFO--> FIRST IN FIRST OUT
from collections import deque

fila = deque([1, 2, 3])
# fila.append(4)
# fila.append(5)
# fila.append(6)
# print(fila)

fila.popleft()
print(fila)

fila.popleft()
print(fila)

fila.popleft()
print(fila)
if not fila: #[]lista vacia es false, " ", el cero 0
    print("No tiene todavia")