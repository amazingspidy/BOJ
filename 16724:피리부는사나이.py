import sys
from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
d = ["U", "D", "L", "R"]
visited = [[0] * M for _ in range(N)]

answer = 0


def dfs(x, y, cnt):
  global visited
  global answer
  if visited[x][y] == 0:
    visited[x][y] = cnt

  temp = d.index(arr[x][y])
  dx, dy = dxy[temp]
  nx, ny = x + dx, y + dy
  temp2 = d.index(arr[nx][ny])

  if visited[nx][ny] != 0:
    if visited[nx][ny] == visited[x][y]:
      visited[x][y] = -1
      answer += 1
      return

  elif (temp == 0 and temp2 == 1) or (temp == 1 and temp2 == 0) or (
      temp == 2 and temp2 == 3) or (temp == 3 and temp == 2):
    visited[nx][ny] = -1
    answer += 1
    return
  else:
    #print(f"현재명령어는 {d[temp]}이기 때문에 dfs({x+dx},{y+dy}, {cnt})를 조집니다.")
    dfs(x + dx, y + dy, cnt)


count = 0
for i in range(N):
  for j in range(M):
    if visited[i][j] == 0:
      count += 1
      dfs(i, j, count)

print(answer)
'''for i in range(N):
  print(*visited[i])
'''
