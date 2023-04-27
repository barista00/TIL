# 별찍기 - 4(2441)
# N = int(input())
# for i in range(N):
#     print(' '*i, "*"*(N-i),sep="")

# 대표값(2592)
# a = 0
# dict = {}
# for _ in range(10):
#     N = int(input())
#     a += N
#     if N not in dict:
#         dict[N] = 1
#     else:
#         dict[N] += 1
# new_dict = sorted(dict.items(), key=lambda x:x[1])
# print(a//10)
# print(new_dict[-1][0])

# 세로읽기(10798)
# matrix = [list(input()) for _ in range(5)]
# for j in range(15):
#     for i in matrix:
#         try:
#             print(i[j], end="")
#         except:
#             continue

# 박스(9455)
# T = int(input())
# for t in range(T):
#     N, M = map(int, input().split())
#     lst = [list(map(int, input().split())) for _ in range(N)]
#     a = 0
#     for i in range(N):
#         for j in range(M): # 행 우선 순회
#             if lst[i][j] == 1: 
#                 for q in lst[i:]: # True일 경우 1을 찾은 위치부터 열 우선 순회
#                     if q[j] == 0:
#                         a += 1
                    
#     print(a)

# 누울 자리를 찾아라(1652)
# 2자리가 나와도 x로 중간에 끊기면 다시 2자리가 나오는지 확인해야됨
import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
lst = [list(input()) for _ in range(N)]
a = 0
cnt_lst = []

# 행 우선 순회
for i in range(N):
    for j in range(N-1):
        if lst[i][j] == 'X': # 1. i 행에서 X가 등장했나?
            if a == 1: # X가 등장했다? a값 체크 1이면 리스트에 넣고 a를 초기화한다
                cnt_lst.append(a)
                a = 0
        else: # 2. X가 안나왔다? 그럼 '.' 하고 '.'이 같이 붙어있는지 확인
            if lst[i][j] == '.' and lst[i][j+1] == '.': # 붙어있는거 확인 a값을 1로 지정한다
                a = 1
    if a == 1: # 하나의 행을 다 순회했는데 a가 1이다? 그럼 append해줘야지
        cnt_lst.append(a)
        a = 0

b = 0
cnt_lst2 = []
# 열 우선 순회
for i in range(N):
    for j in range(N-1):
        if lst[j][i] == 'X':
            if b == 1:
                cnt_lst2.append(b)
                b = 0
        else:
            if lst[j][i] == '.' and lst[j+1][i] == '.':
                b = 1
    if b == 1:
        cnt_lst2.append(b)
        b = 0

print(len(cnt_lst), len(cnt_lst2)) 