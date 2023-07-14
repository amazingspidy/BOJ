#풀이 다익스트라.
# 기존의 다익스트라에서 조금의 변형을 가함.

import sys
from collections import deque, defaultdict
import heapq
import copy
import itertools
from bisect import bisect_left

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
weights = [-1] * (n + 1)
MAX = 1e10

for i in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((z, y))
  graph[y].append((z, x))


def dijikstra(start: int):
  heap = []
  heapq.heappush(heap, (-MAX, start))  # 무게선, 노드 순서

  while heap:
    weight, node = heapq.heappop(heap)
    if weights[node] > -weight:
      continue
    for wei, next_node in graph[node]:
      temp = min(-weight, wei)
      if temp > weights[next_node]:
        weights[next_node] = temp
        heapq.heappush(heap, (-temp, next_node))


start, end = map(int, input().split())
dijikstra(start)
print(weights[end])
