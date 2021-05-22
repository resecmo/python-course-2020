import numpy as np

n, m, k = map(int, input().split())
mat = np.empty(shape=(n, m), dtype=np.int8)
for i in range(n):
    mat[i] = list(map(lambda c: 1 if c == '#' else 0, input()))


def step(field):
    neighbors = np.zeros(shape=(n, m))
    neighbors[1:, :] += field[:-1, :]
    neighbors[:-1, :] += field[1:, :]
    neighbors[:, 1:] += field[:, :-1]
    neighbors[:, :-1] += field[:, 1:]
    neighbors[1:, 1:] += field[:-1, :-1]
    neighbors[:-1, :-1] += field[1:, 1:]
    neighbors[:-1, 1:] += field[1:, :-1]
    neighbors[1:, :-1] += field[:-1, 1:]

    field[neighbors < 2] = 0
    field[neighbors == 3] = 1
    field[neighbors > 3] = 0


for i in range(k):
    step(mat)
for row in mat:
    for ch in row:
        print((".", "#")[ch], end="")
    print()
