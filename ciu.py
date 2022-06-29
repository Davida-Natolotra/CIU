from math import floor, pi
from itertools import permutations, combinations, repeat


def generate(comb):
    
    ls = []
    cd = []

    for i in comb:
        s = int(''.join(map(str,i)),16)
        k = floor(s % pi)
        d = ''.join(map(str,i))+str(k)
        ls.append(d)
        cd.append(k)

    print(f"ls = {ls}, len = {len(ls)}")
    f = open("ciu_ls.txt", "x")
    f.write(str(ls))
    f.close()
    return ls

def check(ls):
    for p in range(len(ls)):
        k = floor(int(ls[p][:4]) % pi)
        d = int(ls[p][4])
        chk = False
        if k == d:
            chk = True
        print(chk)


rg = [0,1,2,3,4,5,6,7,8,9,'A','B','C']

def gen4():
    cd1 = []
    for i in rg:
        for j in rg:
            for  k in rg:
                for p in rg:
                    cd1.append(str(i)+str(j)+str(k)+str(p))
    print(f"cd1 = {cd1}, len = {len(cd1)}")     
    return cd1           

nl = generate(permutations(rg,8))
# n2 = generate(permutations(rg,4))
# ps = []
# for nb in nl:
#     for n2b in n2:
#         ps.append(nb+n2b)
# print(f"ps = {ps}, len = {len(ps)}")    
