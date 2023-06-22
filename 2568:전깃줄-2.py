import sys
from collections import deque, defaultdict
import heapq
import copy
import itertools
from bisect import bisect_left

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[0])
vec = []
p = []

for i in range(n):
  if i == 0:
    vec.append(arr[i][1])
  else:
    if arr[i][1] > vec[-1]:
      vec.append(arr[i][1])
    else:
      vec[bisect_left(vec, arr[i][1])] = arr[i][1]

  p.append(bisect_left(vec, arr[i][1]) + 1)

res = []
#print(vec)
#print(p)
k = len(vec)
print(n - k)
for i in range(len(p) - 1, -1, -1):
  if p[i] == k:
    k -= 1

  else:
    res.append(arr[i][0])
for v in res[::-1]:
  print(v)
