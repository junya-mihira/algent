H, W = list(map(int, input().split()))
A = []
for i in range(H):
    a = input()
    A.append(a)

cost = [[0]*W for _ in range(H)]
cost[0][0] = 1

for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            continue
        if i > 0:
            cost[i][j] += cost[i-1][j]
        if j > 0:
            cost[i][j] += cost[i][j-1]

print(cost[H-1][W-1])
