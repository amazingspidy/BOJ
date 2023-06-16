import sys
from collections import deque, defaultdict
import heapq
import copy

MOD = 1_000_000_000
N = int(input())

dp = [[[0] * (1 << 10) for ending_num in range(10)]
      for jari_soo in range(N + 1)]

#dp[bitmask][jarisoo][ending number] 비트정보, 현재수의 자리수, 끝나는수

for i in range(1, 10):
  dp[1][i][1 << i] = 1
  # 자리수가 1이고, i로 끝나는 수들은 1개씩있음

for i in range(2, N + 1):
  for j in range(10):
    for k in range(0, 1 << 10):
      if j == 0:
        dp[i][j][k | (1 << j)] += dp[i - 1][1][k]
      elif j == 9:
        dp[i][j][k | (1 << j)] += dp[i - 1][8][k]

      else:
        dp[i][j][k | (1 << j)] += (dp[i - 1][j - 1][k] + dp[i - 1][j + 1][k])

ans = 0
for i in range(10):
  ans += dp[N][i][(1 << 10) - 1]
  ans %= MOD
print(ans)
