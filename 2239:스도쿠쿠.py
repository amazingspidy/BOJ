import sys
from collections import deque, defaultdict
import heapq

input = sys.stdin.readline
arr = [[0] * 9 for _ in range(9)]
for i in range(9):
  line = input()
  for j in range(9):
    arr[i][j] = int(line[j])

blank = []
for i in range(9):
  for j in range(9):
    if arr[i][j] == 0:
      blank.append((i, j))


def find_empty(x, y, num):
  """find empty number by searching row, col, 3x3 boundary"""
  for i in range(9):
    if arr[x][i] == num:
      return False

    if arr[i][y] == num:
      return False

  bx, by = x // 3, y // 3
  for i in range(bx * 3, bx * 3 + 3):  #3x3
    for j in range(by * 3, by * 3 + 3):
      if arr[i][j] == num:
        return False
  return True


def backtracking(idx):
  if idx == len(blank):
    for i in range(9):
      for j in range(9):
        print(arr[i][j], end='')
      print()
    sys.exit()

  x, y = blank[idx][0], blank[idx][1]

  for i in range(1, 10):
    if find_empty(x, y, i):
      arr[x][y] = i
      backtracking(idx + 1)
      arr[x][y] = 0


backtracking(0)
