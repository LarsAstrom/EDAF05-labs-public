import sys
def inv_list(l):
    out = [0]*(N+1)
    for i in range(N):
        out[l[i]] = i
    return out

inp_file = sys.argv[1]
with open(inp_file) as f: lines = f.read().strip().split('\n')
N = int(lines[0])
women = [[] for _ in range(N+1)]
men = [[] for _ in range(N+1)]
allinp = [int(x) for line in lines[1:] for x in line.split()]
for person in range(2*N):
    person_inp = allinp[person*(N+1):(person+1)*(N+1)]
    person_id = person_inp[0]
    person_inv_pref_list = inv_list(person_inp[1:])
    if women[person_id]: men[person_id] = person_inv_pref_list
    else: women[person_id] = person_inv_pref_list

pairs = []
allMen = []
for woman in range(1,N+1):
    man = int(input())
    allMen.append(man)
    assert 1<=man<=N, 'Man index out of range'
    pairs.append((woman,man))
if len(set(allMen)) < N:
    print('Fail')
    exit()
for w1,m1 in pairs:
    for w2,m2 in pairs:
        if w1 == w2: continue
        if men[m1][w2] < men[m1][w1] and women[w2][m1] < women[w2][m2]:
            print('Fail')
            exit()
        if men[m2][w1] < men[m2][w2] and women[w1][m2] < women[w1][m1]:
            print('Fail')
            exit()
print('success')
