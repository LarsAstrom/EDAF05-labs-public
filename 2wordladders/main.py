import fileinput
from collections import deque
import time

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

def build_graph():
    words = list()
    queries = list()

    graph = list()

    N = 0

    for i, line in enumerate(fileinput.input()):
        line = line.strip()

        if fileinput.isfirstline():
            line = line.split(" ")
            N = int(line[0])

            graph = [[] for x in range(N)]
        elif i <= N:
            for w_i, w in enumerate(words):
                if check_if_neighbour(line, w):
                    graph[i-1].append(w_i)
                
                if check_if_neighbour(w, line):
                    graph[w_i].append(i-1)
            
            words.append(line)
        else:
            q = line.split(" ")
            queries.append((q[0], q[1]))

    return words, queries, graph, N

def check_if_neighbour(w, n):
    letters = w[-4:]
    for l in letters:
        if letters.count(l) > n.count(l):
            return False
    
    return True

if __name__ == "__main__":
    t1 = time.time()
    words, queries, G, N = build_graph()
    #print(time.time() - t1)
    for q in queries:
        s = words.index(q[0])
        t = words.index(q[1])
        res = bfs(G, s, t, N)
        
        if res != None:
            n = 0
            w = t
            while w != s:
                w = res[w]
                n = n + 1
            
            print(n)
        else:
            pass
            print("Impossible")

    