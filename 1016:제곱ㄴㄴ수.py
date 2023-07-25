import sys
import math
input = sys.stdin.readline

MIN, MAX = map(int, input().split())
n = MAX - MIN + 1

array = [1 for i in range(n)]

for i in range(2, int(math.sqrt(MAX)) + 1):
  j = MAX // (i**2)
  #print(f"{i}를 실행중입니다. {j}는 뭡니까")
  while MIN <= i * i * j <= MAX:
    array[i * i * j - MIN] = 0
    #print(f"{i*i*j}를 지웁니다. i는 {i}입니도, j는 {j}입니도")
    j -= 1

print(sum(array))
