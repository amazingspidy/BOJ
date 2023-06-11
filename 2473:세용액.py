#sliding window (two pointer)
#하나의 변수를 고정시키고 투포인터로 탐색하자.
import sys
from collections import deque, defaultdict
import heapq

input = sys.stdin.readline
N = int(input())
l = list(map(int, input().split()))
l.sort()
mmin = 1e15


def two_pointer(LIST: list):
  global mmin
  answer = [0, 0, 0]

  for i in range(N - 1):
  #여기서 start를 i+1로 고정시킬수 있는 이유는, 모든경우의수를 따져보면
  # fixed 이후에 start가 나오더라도 모든 경우를 커버가 가능함.
    fixed = LIST[i]
    start, end = i + 1, N - 1

    while start < end:
      temp = fixed + LIST[start] + LIST[end]
      if temp == 0:
        return fixed, LIST[start], LIST[end]
        sys.exit()

      if abs(temp) < mmin:
        mmin = abs(temp)
        answer = fixed, LIST[start], LIST[end]

      if temp < 0:
        start += 1

      else:
        end -= 1

  return answer


ans = two_pointer(l)
ans2 = list(ans)
ans2.sort()
print(*ans2)
