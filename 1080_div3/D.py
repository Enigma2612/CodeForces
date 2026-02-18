for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))

    ans = [0]*n
    for i in range(n):
        for j in range(n):
            ans[i] += -(abs(i-j)+1)*lis[j]
    print(ans)