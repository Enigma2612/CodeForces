x1, y1 = list(map(int, input().split()))
directions = input()

dir_map = {'U':0, 'D':0, 'L':0, 'R':0}
for i in directions:
    dir_map[i] += 1

x2 = x1 + dir_map['R'] - dir_map['L']
y2 = y1 + dir_map['U'] - dir_map['D']

print(x2, y2)
