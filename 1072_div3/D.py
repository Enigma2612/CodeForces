for _ in range(int(input())):
    n,k = list(map(int, input().split()))

    if not k:
        print(n)
        continue

    findable = set()
    used = set()

    def mark_findables(num,n,k):
        if (num,k) in used:
            return
        if k > 0:
            findable.add(num)
            used.add((num, k))
            mark_findables(num+1, n, k-1)
            mark_findables(num*2, n, k-1)

    mark_findables(1, n, k)

    print(max(n - len(findable), 0))


#TLE