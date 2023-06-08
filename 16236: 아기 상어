import sys
from collections import deque, defaultdict
import heapq

#type1 : 상어 거리와 x,y좌표를 list에 넣고 sort하는 방식
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0,-1,1,0]
dy = [1,0,0,-1]
size_shark = 2
shark_eats = 0
def bfs(start: (int, int)):
  global size_shark, shark_eats
  visited = [[-1]*N for _ in range(N)]
  dq = deque()
  visited[start[0]][start[1]] = 0
  dq.append(start)

  eaten = []
  
  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0<=nx<N and 0<=ny<N and visited[nx][ny]==-1 and arr[nx][ny] <= size_shark):
        dq.append((nx, ny))
        visited[nx][ny] = visited[x][y] + 1
        if arr[nx][ny]!=0 and arr[nx][ny] < size_shark:
          eaten.append((nx, ny, visited[nx][ny]))
          
  
  if len(eaten) == 0:
    return False
  eaten.sort(key = lambda x:(x[2], x[0], x[1])) 
  return eaten[0] #가장 조건에 부합하는 녀석.
  
start_point = (0,0)
for i in range(N):
  for j in range(N):
    if arr[i][j] == 9:
      arr[i][j] = 0
      start_point = (i, j)

total_time = 0

while True:
  next_point = bfs(start_point)
  arr[start_point[0]][start_point[1]] = 0
  if next_point == False:
    break 
  else:
    start_point = (next_point[0], next_point[1]) 
  
  total_time += next_point[2]
  shark_eats += 1
  if shark_eats == size_shark:
    size_shark += 1
    shark_eats = 0
print(total_time)
  



#type 2 -> 모든 sorting은 결국 부등호비교로 대체가능하다! (부등호로 실행속도 개선)
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]
size_shark = 2
shark_eats = 0


def bfs(start: (int, int)):
  global size_shark, shark_eats
  mx, my, md = 1e9, 1e9, 1e9
  visited = [[-1] * N for _ in range(N)]
  dq = deque()
  visited[start[0]][start[1]] = 0
  dq.append(start)

  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1
          and arr[nx][ny] <= size_shark):
        dq.append((nx, ny))
        visited[nx][ny] = visited[x][y] + 1
        if arr[nx][ny] != 0 and arr[nx][ny] < size_shark:
          if md > visited[nx][ny]:
            mx, my, md = nx, ny, visited[nx][ny]
          elif md == visited[nx][ny]:
            if mx > nx:
              mx, my, md = nx, ny, visited[nx][ny]
            elif mx == nx:
              if my > ny:
                mx, my, md = nx, ny, visited[nx][ny]

  if md == 1e9:
    return False
  return (mx, my, md)


start_point = (0, 0)
for i in range(N):
  for j in range(N):
    if arr[i][j] == 9:
      arr[i][j] = 0
      start_point = (i, j)

total_time = 0

while True:
  next_point = bfs(start_point)
  arr[start_point[0]][start_point[1]] = 0
  if next_point == False:
    break
  else:
    start_point = (next_point[0], next_point[1])

  total_time += next_point[2]
  shark_eats += 1
  if shark_eats == size_shark:
    size_shark += 1
    shark_eats = 0
print(total_time)


           
        
  
