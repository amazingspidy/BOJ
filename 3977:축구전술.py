import sys
from collections import deque, defaultdict
import math

sys.setrecursionlimit(10**7)
input = sys.stdin.readline
t = int(input())
for i in range(t):
  if i > 0:
    _ = input()
  V, E = map(int, input().split())
  graph = [[] for _ in range(V)]
  parents = [0] * (V)
  stack = []
  finished = [False] * (V)
  id = 0
  ans = []
  for i in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

  def SCC(idx):
    global id, ans
    id += 1
    root = parents[idx] = id
    stack.append(idx)

    for v in graph[idx]:
      if not parents[v]:  #초기 세팅상으로 되어있으면
        root = min(root, SCC(v))  #root가 작은값일수록 초반애들임.
      elif not finished[v]:
        root = min(root, parents[v])

    if root == parents[idx]:
      scc_set = []
      while stack:
        p = stack.pop()
        scc_set.append(p)
        finished[p] = True
        if idx == p:
          break
      ans.append(scc_set)

    return root

  for i in range(V):
    if not parents[i]:
      SCC(i)

  last_visited = [0] * (V)
  answer = len(ans)

  scc_dict = {}
  for i in range(len(ans)):
    for an in ans[i]:
      scc_dict[an] = i

  count = [0] * (len(ans))
  q = deque()
  for i in range(len(ans)):
    if last_visited[ans[i][0]] == 0:
      last_visited[ans[i][0]] = 1
      q.append(ans[i][0])

    while q:
      now = q.popleft()
      #print(f"now = {now}입니다.")
      for nex in graph[now]:
        if last_visited[nex] == 0:
          last_visited[nex] = 1
          q.append(nex)

        if scc_dict[nex] == scc_dict[now]:
          continue
        else:
          count[scc_dict[nex]] += 1

  for i in range(len(count)):
    if count[i] != 0:
      answer -= 1
    else:
      save = i

  if answer == 1:
    temp = ans[save]
    temp.sort()
    for v in temp:
      print(v)

  else:
    print("Confused")
  print()
