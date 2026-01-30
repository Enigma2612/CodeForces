for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    s = input()
    req_order = [bool(ord(i)-ord("B")) for i in s]
    cur_order = [True]*n
    penalties = list(map(int, input().split()))

    def cost_at_index_when_steps_left(i,k):

        if i==n or k==0:
            return sum([penalties[p] for p in range(n) if req_order[p] != cur_order[p]])
        jake = i+1
        for j in range(i, n):
            if not req_order[j]:
                break
            else:
                cur_order[j] = False
                jake = j+1
        
        x = cost_at_index_when_steps_left(jake+1, k-1)
        y = cost_at_index_when_steps_left(i+1, k)

        return min(x,y)
    
    print(cost_at_index_when_steps_left(0,k))
