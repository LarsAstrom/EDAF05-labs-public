import sys
def get_score(s1,s2):
    sc = 0
    for i in range(len(s1)):
        if s1[i] == s2[i] == '*': sc += -8
        elif s1[i] == '*': sc += -4
        elif s2[i] == '*': sc += -4
        else: sc += blosum[s1[i]][s2[i]]
    return sc

def valid_string(s,s2):
    s3 = []
    for ch in s2:
        if ch != '*': s3.append(ch)
    return s == ''.join(s3)

inp_file = sys.argv[1]
out_file = sys.argv[2]
ans_file = sys.argv[3]
with open(inp_file) as f: lines = f.read().strip().split('\n')
with open(out_file) as fo: lines_out = fo.read().strip().split('\n')
with open(ans_file) as fa: lines_ans = fa.read().strip().split('\n')
chs = lines[0].split()
blosum = {ch:{} for ch in chs}
for i in range(len(chs)):
    gains = list(map(int,lines[i+1].split()))
    for j in range(len(chs)):
        blosum[chs[i]][chs[j]] = gains[j]

Q = int(lines[len(chs)+1])
for q in range(Q):
    s1,s2 = lines[len(chs)+2+q].split()
    so1,so2 = lines_out[q].split()
    if len(so1) != len(so2):
        print('fail, strings of unequal length')
        exit()
    sa1,sa2 = lines_ans[q].split()
    if not (valid_string(s1,so1) and valid_string(s2,so2)):
        print('fail, invalid string')
        exit()
    out_score, ans_score = get_score(so1,so2), get_score(sa1,sa2)
    if out_score < ans_score:
        print('fail, too small gain. Got {}, expected {}.'.
                format(out_score,ans_score))
        exit()
    if out_score > ans_score:
        print('uhoh, too large gain, got {}, expected {}'.
                format(out_score,ans_score))
        exit()
print('success')
