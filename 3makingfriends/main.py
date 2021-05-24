import fileinput
import time
import math

def mst_kruskal(E, V):
    T = []
    B = E

    parent = []
    for n in V:
        parent.append(n - 1)

    rank = [1] * len(V)

    while len(B) != 0:
        e = B.pop()
        u = e[0]
        v = e[1]

        x = find(parent, u - 1)
        y = find(parent, v - 1)

        if x != y:
            T.append(e)
            union(parent, rank, x, y)

    return T

# Union by rank
def union(parent, rank, x, y):
    x = find(parent, x - 1) - 1
    y = find(parent, y - 1) - 1

    if rank[x] < rank[y]:
        parent[x] = y
        rank[y] += rank[x]
    else:
        parent[y] = x
        rank[x] += rank[y]
    #else:
        #parent[y] = x
        #rank[x] += 1


def find(parent, u_i):
    if parent[u_i] == u_i:
        return u_i + 1
    else:
        return find(parent, parent[u_i])


def load_data():
    N = 0
    M = 0

    E = list()
    V = set()
    for line in fileinput.input():
        line = line.strip().split(" ")
        line = list(map(int, line))

        if fileinput.isfirstline():
            N = line[0]
            M = line[1]
        else:
            E.append(line)

            V.add(line[0])
            V.add(line[1])

    E.sort(key = lambda n: n[2], reverse=True)

    return E, V, N, M



if __name__ == "__main__":
    E, V, N, M = load_data()
    T = mst_kruskal(E, V)

    cost = 0
    for e in T:
        cost += e[2]

    print(cost)

