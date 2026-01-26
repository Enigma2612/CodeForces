def bin_search(val, lis, n):
    a = 0
    b = n-1

    ans = -1
    
    while a<=b:
        x = a + (b-a)//2

        if lis[x] <= val:
            ans = x
            a = x + 1
        else:
            b = x - 1

    return ans+1