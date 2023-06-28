import sys
from collections import deque, defaultdict
import heapq
import copy
import itertools
from bisect import bisect_left


#dfs+dp 문제.
#교훈: 어차피 dfs는 visited배열을 기반으로 돌기때문에 적정한 크기에 대해서는 for문으로 모든 배열을
#탐색하면서 dp+dfs를 돌려줘도 된다. top-down구조에 dfs가 적절히 섞인 문제.
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dp = [[0] * n for _ in range(n)]


def dfs(x, y):
  #print(f"{x} {y} 에서 진행중----------")
  """for i in range(n):
    print(*dp[i])"""

  if dp[x][y] != 0:
    return dp[x][y]

  for i in range(4):
    nx, ny = x + dxy[i][0], y + dxy[i][1]
    if (0 <= nx < n and 0 <= ny < n):
      if arr[nx][ny] > arr[x][y]:
        dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
  return dp[x][y]


answer = 0
for i in range(n):
  for j in range(n):
    answer = max(answer, dfs(i, j))
print(answer + 1)
