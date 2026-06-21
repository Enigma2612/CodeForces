for _ in range(int(input())):
    a,b,x = list(map(int, input().split()))

    ans = abs(a-b)
    m = max(a,b)
    c = 0
    while m > 0:
        m,m2 = max(a,b), min(a,b)
        c += 1
        ans2 = abs(m//x - m2) + c
        ans = min(ans, ans2)

        a,b = m//x, m2

    print(ans)