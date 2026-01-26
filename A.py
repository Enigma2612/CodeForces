for _ in range(int(input())):
    n,s,x = list(map(int, input().split()))
    lis = list(map(int, input().split()))
    diff = s - sum(lis)
    
    if diff % x or diff < 0:
        print("NO")
    else:
        print("YES")