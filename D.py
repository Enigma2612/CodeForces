def bin_search(val, lis, n):
    a = 0
    b = n-1

    ans = -1
    
    while a <= b:
        x = a + (b-a)//2

        if lis[x] <= val:
            ans = x
            a = x + 1
        else:
            b = x - 1

    return ans+1
    


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()

    a_cum_count = {}
    for i in a:
        a_cum_count[i] = a_cum_count.get(i, 0) + 1
    
    a_set = sorted(a_cum_count.keys())

    for i in range(len(set(a))-2, -1, -1):
        a_cum_count[a_set[i]] += a_cum_count.get(a_set[i+1], 0)
    

    b_cum = b.copy()

    for i in range(1, len(b)):
        b_cum[i] += b_cum[i-1]

    ans = 0
    final_level = 0
    final_x = 0

    for x in a_set:
        s_count = a_cum_count[x]
        level = bin_search(s_count, b_cum, n)
    
        ans = max(ans, (level)*x)

        if ans == level*x:
            final_x = x
            final_level = level

    print(ans)


#Binary search working, but still TLE