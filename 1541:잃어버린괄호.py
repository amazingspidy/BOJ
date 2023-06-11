import sys
from collections import deque, defaultdict
import heapq

input = sys.stdin.readline
total_formula = list(input().split('-'))
partial_formula = []

for p in total_formula:
  temp = list(map(int, p.split("+")))
  hap = sum(temp)
  partial_formula.append(hap)

ans = partial_formula[0]
for i in range(1, len(partial_formula)):
  ans -= partial_formula[i]

print(ans)
