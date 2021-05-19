import fileinput
from collections import deque

def bfs(G, s, t, N):
    visited = [0] * N
    visited[s] = 1
    q = deque([s])
    pred = dict()
    
    if s == t:
        return dict({s: t})

    while q != deque([]):
        v = q.popleft()

        for w in G[v]:
            if not visited[w]:
                visited[w] = 1
                q.append(w)
                pred[w] = v
        
            if w == t:
                return pred

    return None

def edmonds_karp(graph, source, sink, N, P):
    
    parent = [-1] * N
    max_flow = 0
    flow = [0] * P

    path = bfs(graph, source, sink, N)
    print("path", P)
    while P != None:
        
        n = sink
        bn = float("Inf")
        while n != source:
            bn = min(bn, graph[path[n]][n])
            n = path[n]
        
        print(bn)
        

        

def load_data():

    N = 0
    M = 0
    C = 0
    P = 0

    routes = list()
    del_routes = list()
    graph = list()

    for i, line in enumerate(fileinput.input()):
        line = line.strip().split(" ")
        line = list(map(int, line))

        if fileinput.isfirstline():
            N = line[0]
            M = line[1]
            C = line[2]
            P = line[3]

            graph = [dict() for x in range(N)]
        elif i <= M:
            u = line[0]
            v = line[1]
            c = line[2]

            routes.append((u,v))

            graph[u][v] = c
            graph[v][u] = c

        else:
            del_routes.append(line[0])

    return (N, M, C, P), routes, del_routes, graph

if __name__ == "__main__":
    (N, M, C, P), routes, del_routes, graph = load_data()
    print(edmonds_karp(graph, 0, N-1, N, P))