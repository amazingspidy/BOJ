import sys
from collections import deque, defaultdict
import heapq
import copy

input = sys.stdin.readline
t = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(t):
  h, w = map(int, input().split())
  arr = [['.'] * (w + 2) for _ in range(h + 2)]
  for i in range(1, h + 1):
    s = input()
    for j in range(1, w + 1):
      arr[i][j] = s[j - 1]
  key = {}
  k = input()[:-1]
  if k != "0":
    for v in k:
      key[v] = 1
  #print(key)
  visited_doc = []

  def bfs():

    dq = deque()
    dq.append((0, 0))
    visited = [[-1] * (w + 2) for _ in range(h + 2)]
    visited[0][0] = 0  #방문

    while dq:
      x, y = dq.popleft()
      for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < h + 2 and 0 <= ny < w + 2 and visited[nx][ny] == -1
            and arr[nx][ny] != "*"):

          if arr[nx][ny] == "$" and (nx, ny) not in visited_doc:
            visited_doc.append((nx, ny))
            dq.append((nx, ny))
            visited[nx][ny] = 0  #방문

          elif arr[nx][ny].islower():  #키를 얻었을때
            if arr[nx][ny] in key:  #있던키 획득
              #print(f"이미 있던키 {arr[nx][ny].lower()} 를 얻었다")
              visited[nx][ny] = 0  #방문
              dq.append((nx, ny))
            else:  #새로운 키를 얻으면
              key[arr[nx][ny].lower()] = 1
              #print(f"key {arr[nx][ny].lower()}를 얻었다")
              visited = [[-1] * (w + 2) for _ in range(h + 2)]
              #방문 초기화
              visited[nx][ny] = 0
              dq.clear()
              dq.append((nx, ny))
          elif arr[nx][ny].isupper():  #문일때
            if arr[nx][ny].lower() in key:
              #print(f"문 {arr[nx][ny]}를 열었다")
              visited[nx][ny] = 0  #방문
              dq.append((nx, ny))
            else:
              continue
              #방문 x
          else:  #그냥 길인경우
            visited[nx][ny] = 0  #방문
            dq.append((nx, ny))

    print(len(visited_doc))

  bfs()
