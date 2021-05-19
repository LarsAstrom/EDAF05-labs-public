import fileinput
import math
def closest_pair(px, py, N):

    if N <= 3:
        min_dist = math.inf
        for i in range(N-1):
            for j in range(i+1, N):
                dist = math.dist(px[i], px[j])

                if dist < min_dist:
                    min_dist = dist

        return min_dist


    mid = N // 2
    py_l = px[:mid].sort(key= lambda p: p[1])
    py_r = px[mid:].sort(key= lambda p: p[1])
    dl = closest_pair(px[:mid], py_l, mid)
    dr = closest_pair(px[mid:], py_r, N-mid)
    # Min distance in the halves
    d = min(dl, dr)
    

    # Checking distance between the halves
    xp = px[mid]                
    S = [xp]
    
    i = 1
    while (mid+i < len(px)):
        x_dist = abs(xp[0] - px[mid+i][0])
        if x_dist < d:
            S.append(px[mid+i])
        else:
            break

        i = i + 1

    i = -1
    while (mid+i >= 0):
        x_dist = abs(xp[0] - px[mid+i][0])
        if x_dist < d:
            S.append(px[mid+i])
        else:
            break
        
        i = i - 1

    S.sort(key = lambda p: p[1])
    
    cross_dist = math.inf
    for i in range(len(S)):
        for j in range(i+1, i+16):
            if j == len(S):
                break

            dist = math.dist(S[i], S[j])

            if dist < cross_dist:
                cross_dist = dist
    
    return min(cross_dist, d)

def load_data():
    N = 0
    px = list()
    py = list()

    for line in fileinput.input():
        line = line.strip()

        if fileinput.isfirstline():
            N = int(line)
        else:
            line = list(map(int, line.split(" ")))

            px.append((line[0], line[1]))
            py.append((line[0], line[1]))


            """
            for i in range(len(px)+1):
                print("i:", i, "len", len(px), px)
                if i == len(px):
                    print("last in")
                    px.insert(i, (line[0], line[1]))
                elif line[0] < px[i][0]:
                    print("insert")
                    px.insert(i-1, (line[0], line[1]))
                    break
            
            for i in range(len(py)+1):
                print("i:", i, "len", len(py), py)
                if i == len(py):
                    print("last in")
                    py.insert(i, (line[0], line[1]))
                elif line[1] < py[i][1]:
                    print("insert")
                    py.insert(i-1, (line[0], line[1]))
                    break"""

    px.sort(key= lambda p: p[0])
    py.sort(key= lambda p: p[1])

    return N, px, py

if __name__ == "__main__":
    N, px, py = load_data()
    
    d = closest_pair(px, py, N)
    print(format(round(d, 6), '.6f'))

   



