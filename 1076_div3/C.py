for _ in range(int(input())):
    n, q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = []

    for i in range(n-1, -1, -1):
        if i == n-1:
            a[i] = max(a[i], b[i])
        else:
            a[i] = max(a[i], b[i], a[i+1])

    sum_lis = a.copy()
    for i in range(1, n):
        sum_lis[i] += sum_lis[i-1]

    for _ in range(q):
        l,r = list(map(int, input().split()))

        ans.append(sum_lis[r-1] - (sum_lis[l-2] if l!=1 else 0))
    
    print(*ans)