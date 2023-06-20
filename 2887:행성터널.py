import sys
from collections import deque, defaultdict
import heapq
import copy

input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
  k = list(map(int, input().split()))
  k.append(i)
  arr.append(k)

arr.sort(key=lambda x: x[0])
arr_cha = []
for i in range(len(arr) - 1):
  arr_cha.append([arr[i][3], arr[i + 1][3], abs(arr[i][0] - arr[i + 1][0])])

arr.sort(key=lambda x: x[1])

for i in range(len(arr) - 1):
  arr_cha.append([arr[i][3], arr[i + 1][3], abs(arr[i][1] - arr[i + 1][1])])

arr.sort(key=lambda x: x[2])

for i in range(len(arr) - 1):
  arr_cha.append([arr[i][3], arr[i + 1][3], abs(arr[i][2] - arr[i + 1][2])])


def find_minimum_distance(edges: list) -> int:
  parent = [i for i in range(len(edges) + 1)]

  def find_parent(x):
    if parent[x] != x:
      parent[x] = find_parent(parent[x])
    return parent[x]

  def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
      parent[b] = a
    else:
      parent[a] = b

  edges.sort(key=lambda x: x[2])
  total_cost = 0
  for i in range(len(edges)):
    a, b, cost = edges[i]
    if find_parent(a) != find_parent(b):
      union(a, b)
      total_cost += cost

  return total_cost


print(find_minimum_distance(arr_cha))
