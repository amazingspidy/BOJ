#bfs중에서 굉장히 중요한 유형이다!
#bfs라고 해서 좌표만 큐에 넣을생각만 하지 말고 cnt같은 추가변수도 같이 넣어주면 훨씬더 좋다!
import sys
from collections import deque, defaultdict
import heapq
import copy

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[0] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(N):
  s = input()
  for j in range(M):
    arr[i][j] = s[j]

R_point, B_point, O_point = (0, 0), (0, 0), (0, 0)

for i in range(N):
  for j in range(M):
    if arr[i][j] == "R":
      R_point = (i, j)
    if arr[i][j] == "B":
      B_point = (i, j)
    

dq = deque()
cnt = 1
dq.append((R_point[0], R_point[1], B_point[0], B_point[1], cnt))
visited = []
visited.append((R_point[0], R_point[1], B_point[0], B_point[1]))


def bfs():
  while dq:
    rx, ry, bx, by, cnt = dq.popleft()
    if cnt > 10:
      break

    for i in range(4):
      R_goal_in, B_goal_in = False, False
      nrx, nry = rx, ry
      while True:
        if (0 <= nrx + dx[i] < N and 0 <= nry + dy[i] < M):
          nrx += dx[i]
          nry += dy[i]
          if arr[nrx][nry] == "#":
            nrx -= dx[i]
            nry -= dy[i]
            break
          elif arr[nrx][nry] == "O":
            R_goal_in = True
            break
      nbx, nby = bx, by
      while True:
        if (0 <= nbx + dx[i] < N and 0 <= nby + dy[i] < M):
          nbx += dx[i]
          nby += dy[i]
          if arr[nbx][nby] == "#":
            nbx -= dx[i]
            nby -= dy[i]
            break
          elif arr[nbx][nby] == "O":
            B_goal_in = True
            break

      if B_goal_in:
        continue
      if R_goal_in:
        print(cnt)
        return

      R_goal_in, B_goal_in = False, False
      if nrx == nbx and nry == nby:
        dis_r = max(abs(nrx - rx), abs(nry - ry))
        dis_b = max(abs(nbx - bx), abs(nby - by))
        if dis_r <= dis_b:  #b가 많이간 -> 즉 느리게간.
          nbx -= dx[i]
          nby -= dy[i]
        elif dis_r > dis_b:  # r가 많이간 -> 즉 r이 느리게간.
          nrx -= dx[i]
          nry -= dy[i]

      if (nrx, nry, nbx, nby) not in visited:
        visited.append((nrx, nry, nbx, nby))
        #print(f"nrx={nrx} nry={nry} nbx={nbx} nby={nby} cnt={cnt}")
        dq.append((nrx, nry, nbx, nby, cnt + 1))

  print(-1)


bfs()
