import sys
from collections import deque, defaultdict
import heapq
import copy

input = sys.stdin.readline
R, C, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]


def move(r, c, s, d, z):
  if d == 1:
    if s > r - 1:
      dir = (s - (r - 1)) // (R - 1)
      temp = (s - (r - 1)) % (R - 1)
      if dir % 2 == 0:
        return 1 + temp, c, s, 2, z
      else:
        return R - temp, c, s, 1, z
    else:
      return r - s, c, s, d, z
  if d == 2:
    if s > R - r:
      dir = (s - (R - r)) // (R - 1)
      temp = (s - (R - r)) % (R - 1)
      if dir % 2 == 0:
        return R - temp, c, s, 1, z
      else:
        return temp + 1, c, s, 2, z
    else:
      return r + s, c, s, d, z
  if d == 3:

    if s > C - c:
      dir = (s - (C - c)) // (C - 1)
      temp = (s - (C - c)) % (C - 1)
      if dir % 2 == 0:
        return r, C - temp, s, 4, z
      else:
        return r, 1 + temp, s, 3, z
    else:
      return r, c + s, s, d, z
  if d == 4:
    if s > c - 1:
      dir = (s - (c - 1)) // (C - 1)
      temp = (s - (c - 1)) % (C - 1)
      if dir % 2 == 0:
        return r, 1 + temp, s, 3, z
      else:
        return r, C - temp, s, 4, z
    else:
      return r, c - s, s, d, z


ans = 0
for k in range(1, C + 1):
  #print(f"{k}번째 턴입니다")
  arr_temp = []
  visited = {}
  x1, y1, z1, i1, o1 = 1e9, k, 0, 0, -1
  for x, y, z, i, o in arr:
    if y == k and x1 >= x:
      if x1 > x:
        x1, y1, z1, i1, o1 = x, y, z, i, o
      elif x1 == x:
        if o1 < o:
          x1, y1, z1, i1, o1 = x, y, z, i, o  #잡아갈놈 저장
    arr_temp.append([x, y, z, i, o])
    if (x, y) not in visited:
      visited[(x, y)] = o  #크기저장
    else:
      if visited[(x, y)] < o:
        visited[(x, y)] = o
  arr = []
  for x, y, z, i, o in arr_temp:
    if visited[(x, y)] == o:
      if x == x1 and y == y1 and z == z1 and i == i1 and o == o1:
        #print(f"x좌표: {x},y좌표: {y}, 속력:{z},방향:{i},크기:{o} 를 먹었습니다")
        ans += o

      else:
        #print(f"x좌표: {x},y좌표: {y}, 속력:{z},방향:{i},크기:{o} 가 움직입니다")
        arr.append(list(move(x, y, z, i, o)))

print(ans)
