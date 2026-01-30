_ = int(input())

colors = list(map(int, input().split()))

color_count = {}

for i in colors:
    color_count[i] = color_count.get(i, 0) + 1

s = 0
for i in color_count.values():
    s += 2**(i) - 1

print(s%(10**9 + 7))