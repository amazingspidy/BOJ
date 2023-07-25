import sys
from collections import deque, defaultdict
import heapq
import copy
import itertools
from bisect import bisect_left

input = sys.stdin.readline

k, n = map(int, input().split())
arr = list(map(int, input().split()))
heap = []
visited = {}
max_val = 0
for i in range(k):
  max_val = max(max_val, arr[i])
  heapq.heappush(heap, arr[i])

while n > 1:

  temp = heapq.heappop(heap)
  for i in range(k):
    val = temp * arr[i]
    if len(heap) >= n and val >= max_val:  #이미 남은 길이도 n이넘는데, max_val보다 큰 val은 필요 x
      continue
    if val not in visited:  #중복거르기 -> dictionary 써야 훨씬 빨라짐. 딕셔너리 잘쓰자.
      visited[val] = 1
      heapq.heappush(heap, val)
      max_val = max(max_val, val)
  n -= 1
print(heapq.heappop(heap))
