# 행복한지 슬픈지(10769)
# N = input()
# N = list(N)
# hap = 0
# unhap = 0
# # ':'가 등장하는지 확인하는 코드
# for i in range(len(N)):
#     if N[i] == ':':
#         # N[i]가 ':'라면 뒤에 2개가 -) -( 둘중 어떤건지 확인하고 카운트
#         if N[i:i+3] == [':','-',')']:
#             hap += 1
#         elif N[i:i+3] == [':','-','(']:
#             unhap += 1

# 개수에 따라 조건을 적용해 출력
# if hap > unhap:
#     print('happy')
# elif unhap > hap:
#     print('sad')
# elif unhap == 0 and hap == 0:
#     print('none')
# elif unhap == hap:
#     print('unsure')

# 지능형 기차(2455)
# station = [list(map(int,input().split())) for _ in range(4)]

# start = station[0][1] 
# people = [station[0][1]]

# for i in range(1,4):
#     start = start - station[i][0]
#     people.append(start)
#     start = start + station[i][1]
#     people.append(start)
# print(max(people))

# 바이러스(2606)
# 컴퓨터 수
# com = int(input())
# # 연결된 컴퓨터 수
# connec = int(input())
# mat = [[] for _ in range(com+1)] # 인덱싱은 0부터인데 컴퓨터 번호의 시작은 1부터라 이렇게 적음(0번 컴퓨터가 있다고 생각하고 넣은거)

# # 연결된 수들의 인접리스트 만들기
# for i in range(connec):
#     v1, v2 = map(int, input().split())
#     mat[v1].append(v2)
#     mat[v2].append(v1) # 입력받은 2개의 수가 각각의 인덱스 리스트에 들어가야한다 

# virus = [False] * (com+1) # com이 7이라면 인덱스가 0~6으로 된 리스트가 생성되는데 7번 컴퓨터를 고려할 시 에러가 난다 그래서 + 1 해줘야함
# wait = [1]
# virus[1] = True

# while wait:
#     infect = wait.pop()
    
#     for i in mat[infect]:
#         if virus[i] == False:
#             virus[i] = True
#             wait.append(i)
# print(virus.count(True)-1) # 1번 컴퓨터 본인은 카운트하지 않음

# 연결된 노드끼리 리스트에 넣어서 인접 리스트를 만드는 것
# 첫 스타트를 기점으로 연결된 모든 노드를 순회하도록 스택을 사용하는 것
# 연결되어있는지 체크할 체크리스트를 만드는 것

# 섬의 개수(4963)
# import sys
# # 1을 발견하면 일단 섬이니까 주위에 붙어있는 섬이 있는지 체크하는 함수만든다

# # 주위에 섬있는지 확인하기 위한 좌표리스트
# lst = [(-1,0),(1,0),(0,-1),(0,1),(-1,1),(1,1),(1,-1),(-1,-1)]

# # 좌표리스트를 이용해 섬주위에 섬이있는지 확인하는 함수
# # 섬을 일단 0으로해서 없애버리고 섬 주위가 1이면 i, j를 바꾼값으로 dfs함수 호출해서 똑같은 짓 반복함 
# def dfs(matrix, i, j):
#     if matrix[i][j] == 0:
#         return
#     matrix[i][j] = 0
#     for k in lst: # 섬위치기준에서 8방향으로 찾다가 1이 나오면 함수호출 안나오면 걍 끝
#         new_i = i + k[0] 
#         new_j = j + k[1]
#         if new_i < 0 or new_j < 0 or new_i >= h or new_j >= w: # out of range 나오는 경우 크거나 같다고 한 이유는 들어온 값은 5라고할 때 마지막 인덱스는 4기 때문이다
#             continue
#         if matrix[new_i][new_j] == 1:
#             dfs(matrix, new_i, new_j)

# # 1을 찾는 함수 섬을 찾았으니 카운트 + 1 하고 주위에 있는 섬들을 모조리 없애주는 dfs함수 호출
# def find(h, w, matrix):
#     count = 0
#     for i in range(h):
#         for j in range(w):
#             if matrix[i][j] == 1:
#                 count += 1
#                 dfs(matrix, i, j)
#     return count

# while True:
#     w, h = map(int, sys.stdin.readline().rstrip().split())
#     if w == 0 and h == 0:
#         break
#     matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]
#     print(find(h, w, matrix))

import sys

input = sys.stdin.readline
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(y)]
    visited = matrix
print(visited)