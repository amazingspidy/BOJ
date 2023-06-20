import sys
from collections import deque, defaultdict
import heapq
import copy
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n)]


def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])

  return parent[x]


def union(a, b):
  a = find(a)
  b = find(b)
  if a < b:
    parent[a] = b
  else:
    parent[b] = a


for i in range(m):
  a, b = map(int, input().split())
  if find(a) != find(b):
    union(a, b)
  else:
    print(i + 1)
    sys.exit()
print(0)
