import fileinput
import heapq
import math
from collections import defaultdict

def mst(V, E, W, root):
    T = list()
    Q = []

    for v in V:
        heapq.heappush(Q, v)


    while len(Q) != 0: # räkna upp till N istället
        pass
    return T

def load_data():
    
    N = 0
    M = 0

    V = set()
    E = defaultdict(list)
    W = dict()

    C = list()
    for i, line in enumerate(fileinput.input()):
        line = line.strip()

        if fileinput.isfirstline():
            line = line.split(" ")

            N = line[0]
            M = line[1]

            V = [-1]*(N+1)
            W = [math.inf]*M
            E = [-1]*M

            C = [math.inf]*(N+1)
        else:
            line = line.split(" ")

            u = line[0]
            v = line[1]
            w = line[2]

            E[u] = E[u] + [v]
            E[v] = E[v] + [u]

            if v not in V:
                V.add(v)

            if u not in V:
                V.add(u)

    
    return V, E, W



if __name__ == "__main__":
    V, E, W = load_data()
    print(V, E, W)
    root = V.pop()
    T = mst(V, E, W, root)
