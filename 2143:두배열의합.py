import sys
from collections import deque, defaultdict
import heapq
import copy
import itertools
"""아이디어-> 딕셔너리를 쓰면 좀 시간이 줄것이다 라는 발상에서 시작
A에서 가능한 모든 합은 누적합으로 표현이 가능하다
누적합배열과 combination을 사용하여 A에서 나올수있는 모든 경우를 갖다가
A_visited에다가 적어둔뒤, B도 같은 방식으로 모든 경우의 수를 파악하는데
여기서 포인트는 B는 바로바로 A_visited와 연동시켜서 해당 값이 있는지
판단 하에 ans를 더해준다."""
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A_sum = [0] * (len(A))
B_sum = [0] * (len(B))
A_sum[0], B_sum[0] = A[0], B[0]
A_visited = {}
A_visited[A_sum[0]] = 1

for i in range(1, n):
  A_sum[i] = A_sum[i - 1] + A[i]
  if A_sum[i] in A_visited:
    A_visited[A_sum[i]] += 1
  else:
    A_visited[A_sum[i]] = 1
A_nCr = itertools.combinations(A_sum, 2)

for A1, A2 in A_nCr:
  if A2 - A1 in A_visited:
    A_visited[A2 - A1] += 1
  else:
    A_visited[A2 - A1] = 1

ans = 0
if T - B_sum[0] in A_visited:
  ans += A_visited[T - B_sum[0]]
for i in range(1, m):
  B_sum[i] = B_sum[i - 1] + B[i]
  if T - B_sum[i] in A_visited:
    ans += A_visited[T - B_sum[i]]
    #print(f"A에서 {T-B_sum[i]} B에서  {B_sum[i]} ")
B_nCr = itertools.combinations(B_sum, 2)
#print("경계선")
for B1, B2 in B_nCr:
  if T - (B2 - B1) in A_visited:
    ans += A_visited[T - B2 + B1]
    #print(f"A에서 {T - (B2 - B1)} B에서  {B2 - B1} ")
print(ans)
