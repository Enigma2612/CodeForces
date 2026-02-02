for _ in range(int(input())):
    n,m,h = list(map(int, input().split()))
    lis = list(map(int, input().split()))
    
    new_lis = lis.copy()
    changed = []

    for _ in range(m):
        b,c = list(map(int, input().split()))
        if new_lis[b-1] + c > h:
            while changed:
                b = changed.pop()
                new_lis[b] = lis[b]
        else:
            new_lis[b-1] += c
            changed.append(b-1)
    
    print(*new_lis)
    
