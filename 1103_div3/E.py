for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))

    starters = {}

    count = 1
    cur = lis[0]
    for i in range(n):
        if i == 0:
            continue
        if abs(lis[i] - lis[i-1]) == 1:
            count += 1
            cur = min(lis[i], lis[i-1])
        else:
            starters[cur] = count
            cur = lis[i]
            count = 1
    else:
        starters[cur] = count
        cur = lis[i]
        count = 1
    print(starters)
    