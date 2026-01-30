for _ in range(int(input())):
    n,m,h = list(map(int, input().split()))
    lis = list(map(int, input().split()))
    
    new_lis = lis.copy()

    for _ in range(m):
        b,c = list(map(int, input().split()))
        if new_lis[b-1] + c > h:
            new_lis = lis.copy()
        else:
            new_lis[b-1] += c
    
    print(*new_lis)
