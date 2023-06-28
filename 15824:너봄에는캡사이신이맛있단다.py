import sys
from collections import deque, defaultdict
import heapq
import copy
import itertools
from bisect import bisect_left

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

brr = [(i, val) for i, val in enumerate(arr)]

Q = 1_000_000_007

#분할정복을 통한 2의 거듭제곱. logN의 실행속도. 기본 파이썬에서는 N의 실행속도임
def power(n):
  if n == 0:
    return 1
  if n == 1:
    return 2

  else:
    tmp = power(n // 2) % Q
    if n % 2 == 0:
      return (tmp * tmp) % Q
    else:
      return (tmp * tmp * 2) % Q


ans = 0

if len(arr) == 1:
  print(0)
elif len(arr) == 2:
  print((arr[1] - arr[0]) % Q)
else:
  #여기가 굉장히 핵심인데, 결국에 모든 경우의수를 나열해보면, 
  #arr[i]번째의 요소가 최댓값으로 선정되는 경우와, 최솟값으로 선정되는 경우의 차를 arr[i]와 곱해주면 됨.
  #for문이 돌아가면서 오름차순으로 값들이 커지는데, 결국에 i번째가 최댓값으로 선정될 경우의수는
  #총 2^i - 1 이고, 최솟값으로 선정될 경우의수는 2^(n-i-1) -1 임. 그 둘의 차는 아래 식과 같아지는것.
  for i in range(N):
    ans += arr[i] * (power(i) - power(N - i - 1))
    ans %= Q

  print(ans)
