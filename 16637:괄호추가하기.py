import sys
from collections import deque, defaultdict
import heapq
import copy
import itertools
from bisect import bisect_left

input = sys.stdin.readline
#일단 직선으로 연산하는 함수를 만든다
#브루트포스로 괄호쳐주는 방식을 선택. 어차피 최대 길이 19개.
#최대연산자 그렇게되면 9개정도니까, 10개는 숫자겠고.
MAX = 1e10
n = int(input())
math_expression = input()[:-1]

# 연산자 +-*

possible = []
visited = [0] * (len(math_expression) // 2)

#일단은 브루트포스로 모든 경우의수부터 찾자.
def rotate(n, idx):
  global possible, visited
  total = n // 2

  if idx == total:  #종료조건
    possible.append("".join(map(str, visited)))
    return
  if idx - 1 >= 0:
    if visited[idx - 1] == 0:  #이전녀석이 0이면 다음은 0 or 1
      visited[idx] = 1
      rotate(n, idx + 1)
      visited[idx] = 0
      rotate(n, idx + 1)
    elif visited[idx - 1] == 1:  # 이전녀석이 1이면 다음은 반드시 0
      visited[idx] = 0
      rotate(n, idx + 1)
  elif idx == 0:
    visited[idx] = 1
    rotate(n, idx + 1)
    visited[idx] = 0
    rotate(n, idx + 1)


def calculate(expression: str, pattern: str):
  exp_idx = 0
  num_stack = []
  exp_stack = []
  exp_ver = 0
  temp1 = 0
  for e in expression:
    if e.isdigit():  #숫자면.
      if exp_ver != 0:
        if exp_ver == 1:
          num_stack.append(temp1 + int(e))
        elif exp_ver == 2:
          num_stack.append(temp1 - int(e))
        else:
          num_stack.append(temp1 * int(e))
        exp_ver = 0  #다시 바꿔주고.
      else:
        num_stack.append(int(e))
    else:
      if int(pattern[exp_idx]) == 0:
        exp_stack.append(e)
        exp_ver = 0
      else:
        temp1 = num_stack.pop()  #왼쪽피연산수 뺴주기
        if e == "+":
          exp_ver = 1
        elif e == "-":
          exp_ver = 2
        else:
          exp_ver = 3
      exp_idx += 1
    #print(f"num: {num_stack}, exp: {exp_stack}")

  N = len(num_stack)
  hap = 0
  exp_ver = 0
  for i in range(N):
    if i == 0:
      hap = num_stack.pop(0)
    else:
      if exp_ver == 1:
        hap += num_stack.pop(0)
      if exp_ver == 2:
        hap -= num_stack.pop(0)
      if exp_ver == 3:
        hap *= num_stack.pop(0)
    if i == N - 1:
      break
    exp = exp_stack.pop(0)
    if exp == "+":
      exp_ver = 1
    if exp == "-":
      exp_ver = 2
    if exp == "*":
      exp_ver = 3

  return hap

rotate(n, 0)
ans = -1e10
for p in possible:
  temp = calculate(math_expression, p)
  if temp > ans:
    ans = temp
print(ans)
