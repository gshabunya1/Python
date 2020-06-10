import random
n = int(input("Введите размер списка: "))
A = []
for i in range(n):
    a = random.randint(0, 99)
    A.append(a)
print("Элементы списка А:")
for i in range(1,n):
    print(A[i])

B = [0]
for i in range(1,n):
    b= 0
    for j in range(i):
        b = b + A[j]
    B.append(b)
print("Элементы списка B:")
for i in range(1,n):
    print(B[i])
