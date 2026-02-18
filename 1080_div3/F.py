def is_indep(p1, p2):
    a = p2[0]-p1[0]
    b = p2[1]-p1[1]
    c = p2[2]-p1[2]
    
    D = b**2 - 4*a*c
    return D < 0 or (a==b==0 and c!=0)

for _ in range(int(input())):
    n = int(input())
    parabs = []
    for i in range(n):
        parabs.append(tuple(map(int, input().split())))
    
    indeps = {}
    for i in range(n):
        for j in range(n):
            if is_indep(parabs[i], parabs[j]):
                indeps[i+1] = indeps.get(i+1, [i+1]) + [j+1]

    indeps = {i: set(indeps[i]) for i in indeps}

    len_dic = {}
    for i in indeps:
        val_set = indeps.get(i)
        for x in val_set:
            if x == i: continue
            len_dic[i] = max(len_dic.get(i, 0), len(indeps[x].intersection(val_set)))
    
    for i in range(1, n+1):
        print(len_dic.get(i,1), end= ' ')
    print()