import numpy as np

file1 = input()
file2 = input()
vector = np.array(list(map(float, input().split())))

with open(file1) as file:
    A = []
    for line in file:
        A.append(list(map(np.double, line.split())))
    A = np.array(A)
    A2 = A @ A
with open(file2) as file:
    B = list(map(np.double, file.readline().split()))
    B = np.array(B)
print((A2 @ vector).dot(B))
