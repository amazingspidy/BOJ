import sys
from collections import deque, defaultdict
#위상정렬인데 indegree에다가 더 많은 정보를 넣어줘야하는 문제.
input = sys.stdin.readline

def topo_sort():
  n = int(input())
  graph = [[] for i in range(n + 1)]
  indegree = [0] * (n + 1)
  arr = list(map(int, input().split()))
  m = int(input())

  for i in range(n - 1):
    for j in range(i + 1, n):
      x, y = arr[i], arr[j]
      graph[x].append(y)
      indegree[y] += 1

  for _ in range(m):
    a, b = map(int, input().split())
    if b in graph[a]:
      graph[a].remove(b)
      indegree[b] -= 1
      graph[b].append(a)
      indegree[a] += 1
    else:
      graph[b].remove(a)
      indegree[a] -= 1
      graph[a].append(b)
      indegree[b] += 1

  result = []
  q = deque()

  for i in range(1, n + 1):
    if indegree[i] == 0:
      q.append(i)

  while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)
  if len(result) != n:
    print("IMPOSSIBLE")
  else:
    print(*result)


t = int(input())
for _ in range(t):
  topo_sort()
