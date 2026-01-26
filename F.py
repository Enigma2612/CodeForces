for _ in range(int(input())):
    n, ax, ay, bx, by = list(map(int, input().split()))
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    houses = zip(x,y)
    houses = sorted(houses)
    