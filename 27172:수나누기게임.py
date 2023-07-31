import sys
from collections import deque, defaultdict
import heapq
import copy
import itertools
from bisect import bisect_left
import math

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
original = {}
for a in arr:
  original[a] = 1
MAX_VAL= max(arr)
check = [0 for i in range(MAX_VAL+1)]
for a in arr:
  j = 2
  while a * j <= MAX_VAL:
    if a*j in original:
      check[a*j]-=1
      check[a]+=1
    j+= 1

print(check[a], end=' ')
