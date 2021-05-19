import fileinput
from collections import defaultdict
import time
from tqdm import tqdm

def gale_shapely(W, M):
    p = list(M.keys())
    pairs = dict((el, None) for el in list(range(1, len(M)+1)))

    while len(p) > 0:
        m = p.pop()
        w = M[m].pop(0) # this is dumb
        
        if pairs[w] == None:
            pairs[w] = m
        elif W[w][m-1] < W[w][pairs[w]-1]:
            mw = pairs[w]
            pairs[w] = m
            p.append(mw)
        else:
            p.append(m)

    return pairs
        
def load_data():
    men = dict()
    wom = dict()
    
    data = ""
    for line in fileinput.input():      
        data += " " + line.strip() # this might be dumb
    
    data = data.split(" ")
    n = int(data[1])
    p_count = list([0]*n)
    data = data[2:]
    
    for i in range(n+1, len(data)+1, n+1):
        p_data = data[i-(n+1):i]

        p_i = int(p_data[0])
        prefs = p_data[1:]

        p_count[p_i-1] = p_count[p_i-1] + 1
        if p_count[p_i-1] == 1:
            inv_prefs = [0]*n
            for j, man in enumerate(prefs):
                inv_prefs[int(man) - 1] = j + 1    
            wom[p_i] = inv_prefs

        elif p_count[p_i-1] == 2:
            men[p_i] = list(map(int, prefs))
    
    return wom, men

if __name__ == "__main__":
    W, M = load_data()
    pairs = gale_shapely(W, M)

    for man in pairs.values():
        print(man)

