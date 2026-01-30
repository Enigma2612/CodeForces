for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)

    b_cum = b.copy()
    for i in range(1, n):
        b_cum[i] += b_cum[i-1]
    
    ans = 0
    
    for ind, i in enumerate(b_cum):
        if i > len(a):
            break
        ans = max(ans, a[i-1] * (ind+1))
    
    print(ans)

    #WORKS!
    #Not my own solution, logic taken from a yt video