from collections import deque

N, M = list(map(int, input().split()))

G = []
for _ in range(0, N):
    G.append([])

for _ in range(0, M):
    ai, bi = list(map(int, input().split()))

    G[ai-1].append(bi-1)
    G[bi-1].append(ai-1)

# コスト関数
dist = []
for _ in range(0, 10):
    dist.append(-1)

Q = deque
Q.append(0)
dist[0] = 0

while len(Q) > 0:
    i = Q.popleft()
    for j in G[i]:
        if dist[j] == -1:
            dist[j] = dist[i]+1
            Q.append(j)
if dist[N-1] == 2:
    print('yes')
else:
    print('no')
