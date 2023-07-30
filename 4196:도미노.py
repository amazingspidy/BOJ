import sys
from collections import deque, defaultdict
import heapq
import copy
import itertools
from bisect import bisect_left
import math
#SCC로 그룹만들고, 그룹을 한 점으로 본뒤, indegree가 0인 녀석들의 개수가 답!
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
t = int(input())
for i in range(t):

  V, E = map(int, input().split())
  graph = [[] for _ in range(V + 1)]
  parents = [0] * (V + 1)
  stack = []
  finished = [False] * (V + 1)
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

  for i in range(1, V + 1):
    if not parents[i]:
      SCC(i)

  #print(ans)

  last_visited = [0] * (V + 1)
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

  for c in count:
    if c != 0:
      answer -= 1

  print(answer)
