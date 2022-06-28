from math import floor, pi
from itertools import permutations, combinations

comb = permutations(range(pow(10,2)),4)
ls = []
cd = []

for i in comb:
    s = int(''.join(map(str,i)))
    k = floor(s % pi)
    d = str(s)+str(k)
    ls.append(d)
    cd.append(k)

print(f"ls = {ls}, len = {len(ls)}")

def check():
    for p in range(len(ls)):
        k = floor(int(ls[p][:4]) % pi)
        d = int(ls[p][4])
        chk = False
        if k == d:
            chk = True
        # print(chk)


perm = permutations(range(10),4)

# for l in range(len(perm)):
#     ck = False
#     if perm[l] == comb[l]:
#         ck = True
#     print(ck)