# dict = { 1 : 2, 3 : 4}
# print(list(dict))

# 딕셔너리를 이용해서 반복문 돌릴때 딕셔너리 데이터의 변경이 일어나면 에러가 난다
# 그래서 리스트로 변경해서 해결했음
# 딕셔너리를 리스트로 바꾸면 key값만 리스트에 추가되어진다


# 반복문 가동시 list로 바꾸면 본체 딕셔너리가 아니기때문애 상관이 없는 것 같음
# 그래서 list에 kwy를 빼주면 변수에있는 딕셔너리도 같이 빠져나가기만 해서괜찮은듯
# 본체가 반복문을 돌고있지 않기 때문에 
# import sys
# T = int(input())
# for i in range(1, 1+T):
#     a, b = map(int,sys.stdin.readline().rstrip().split())
#     print(a+b)


# while True:
#     try:
#         a = input()
#         print(a)
#     except EOFError:
#         break

# import sys

# s = sys.stdin.readline()
# print(list(s))

# k, q, l, b, n, p = map(int,input().split())
# N = int(input())
# card = list(range(1, N))
# arr = []
# for i in card:
#     arr.append(i)
# from collections import deque
# a = [1,2,3,4]
# a.append(5)

# print(a)
# b = deque(range(5))
# b.appendleft(1)

# print(b)
# from string import ascii_letters
# lst = [i for i in ascii_letters]
# sen = input()
# li = []
# for i in sen:
#     if i == '(' or i == '{' or i == '[':
#         li.append(i)
#     elif i == ')' or i == '}' or i == ']':
# from collections import deque
# N, K = map(int,input().split())
# lst = deque(range(1, 1+N))
# lst2 = []
# while lst:
#     for _ in range(K-1):
#         deque.append(lst, deque.popleft(lst))
#     lst2.append(deque.popleft(lst))
# print('<', end="")
# for i in lst2:
#     if i != lst2[-1]:
#         print(i, end=", ")
#     else:
#         print(i, end="")
# print('>')

# dict = {'ag': 1, 'ac' : 3, 'ba' : 3}
# dict2 = sorted(dict.items(), key= lambda x:(x[0],x[1]))
# print(dict2)


# N, M = map(int, input().split())
# lst = [list(input()) for _ in range(N)]

# li = []
# # 8X8 행렬 분리
# for a in range(N-8+1): # 8X8 덩어리채로 움직이게 하는 반복문
#     for b in range(M-8+1):
#         var = 0
#         for n in range(a, 8+a):
#             for m in range(b, b+8):  
#                 if lst[a][b] == 'B':
#                     if (a + b + n + m) % 2 == 1 and lst[n][m] != 'W':
#                         var += 1
#                     if (a + b + n + m) % 2 == 0 and lst[n][m] != 'B':
#                         var += 1
#                 else:
#                     if (a + b + n + m) % 2 == 1 and lst[n][m] != 'B':
#                         var += 1
#                     if (a + b + n + m) % 2 == 0 and lst[n][m] != 'W':
#                         var += 1
#         if lst[a][b] == lst[a+7][b+7]:
#             li.append(var)

# print(min(li))
# import sys
# from collections import Counter
# N = int(sys.stdin.readline())
# cards = list(map(int, sys.stdin.readline().split())) 

# M = int(sys.stdin.readline())
# howmany = list(map(int, sys.stdin.readline().split()))

# cards_count = Counter(cards)

# lst = []
# for i in howmany:
#     if i in cards_count: # 딕셔너리랑 리스트랑 if문으로 안에 들어있는지 여부 확인하는 시간차이??
#         print(cards_count[i], end=" ")
#     else:
#         print(0, end=" ")

# import heapq
# N = int(input())

# lst = []
# for _ in range(N):
#     num = int(input())
#     heapq.heappush(lst, num)

# while len(lst) != 0: # for문으로 출력했을 때 나오다가 말았음 왜 그런거지 아아 리스트에서 빼버리면 길이가 짧아지니까 그 길이만큼만 반영하는듯
#     print(heapq.heappop(lst))
# # 왜 heapq.heapify를 안해도 힙으로 잘되냐...
# # 빈 리스트에서 heappush할 때 이미 힙의 상태로 집어넣기 때문에 리스트가 다 채워진 상황에서는 이미 힙의 상태로 정렬되어있다
# # 그래서 heapify는 이미 자료가 들어가있는 리스트에서 힙으로 변환할 때 사용하는 것이고
# # 빈 리스트라면 굳이 heapify를 안써도 된다

# import heapq, sys

# N = int(sys.stdin.readline())
# heap = []

# for i in range(N):
#     num = int(sys.stdin.readline())
#     heapq.heappush(heap, num)

# for i in range(len(heap)):
#     sys.stdout.write(str(heapq.heappop(heap))+'\n')

# x, y = map(str, input().split())

# def rev(a):
#     lst = list(reversed(str(a)))
#     re = lst[0]
#     for i in range(1,len(lst)):
#         re = re + lst[i]
#     return int(re)

# print(rev(rev(x)+rev(y)))

# import sys
# sys.stdin = open('input.txt', 'r')

# while True:
#     n, m = map(int, input().split())
#     if n == 0 and m == 0:
#         break

#     lst = []
#     for _ in range(m):
#         lst.append(list(map(int, input().split())))

#     def dfs(x, y):
#         if x <= -1 or x >= m or y <= -1 or y >= n:
#             return False
#         if lst[x][y] == 1:
#             lst[x][y] = 0

#             dfs(x+1,y)
#             dfs(x-1,y)
#             dfs(x,y+1)
#             dfs(x,y-1)
#             dfs(x+1,y-1)
#             dfs(x-1,y+1)
#             dfs(x+1,y+1)
#             dfs(x-1,y-1)
#             # 재귀함수 호출 하면 발생하는 상황을 머릿속에 잘 시뮬 돌리면 더 잘 이해될듯
#             return True
#         return False
    
#     land = 0
#     for i in range(m):
#         for j in range(n):
#             if dfs(i, j) == True:
#                 land += 1
#     print(land)



# from collections import Counter
# import sys
# sys.stdin = open('input.txt', 'r')

# N = int(input())
# li = []

# for _ in range(N):
#     string = input()
#     li.append(string)

# counter = Counter(li)
# num_li = []
# for i in counter:
#     num_li.append(counter[i])

# sort_counter = sorted(counter.items(), key=lambda x : (x[1], x[0])) # 개수 작은 것부터 큰 순으로 정렬하면서 사전 순으로 앞에 오는순

# for i in sort_counter: # 개수가 가장 크면서 사전순으로 맨앞에 있는 경우를 출력함
#     if i[1] == max(num_li):
#         print(i[0])
#         break




# a, b = input().split()

# set1 = set(map(int, input().split()))
# set2 = set(map(int, input().split()))

# result_set = set1 - set2

# sort_result_set = sorted(result_set, key= lambda x:x)
# # print(result_set)
# if result_set == set(): # set끼리 빼서 차집합했을 때 결과가 빈 set이면 set()로 출력된다...? 
#                         # 그냥 {}를 사용하면 딕셔너리이다 빈 세트는 set()로 표현한다
#     print(0)
# else:
#     print(len(sort_result_set))
#     print(*sort_result_set)

# N, M = map(int, input().split())

# lst = [[] for _ in range(N+1)] # 그냥 리스트 [] * N 하는거랑 다른 결과다
# for _ in range(M):
#     num1, num2 = map(int, input().split())
#     lst[num1].append(num2)
#     lst[num2].append(num1)
# # print(lst)

# visited = [False] * (N+1)

# def dfs(a):
#     start = [a]
#     visited[a] = True
#     while True:
#         if start == []:
#             break
#         else:
#             start_pop = start.pop()

#             for i in lst[start_pop]:
#                 if visited[i] == False:
#                     visited[i] = True
#                     start.append(i)


# cnt = 0
# for i in range(1,N+1):
#     if visited[i] == False:
#         cnt += 1
#         dfs(i)
# print(cnt)
# # 재귀함수 활용을 좀 해보면 좋을 것 같다 지금 상황은 좀 쓸데없이 동작한느 코드가 많은듯 함

# N = int(input())
# person1, person2 = map(int, input().split())
# M = int(input())

# lst = [[] for _ in range(N+1)]
# visited = [False] * (N+1)

# for _ in range(M):
#     a, b = map(int, input().split())
#     lst[a].append(b)
#     lst[b].append(a)

# cnt = 0
# stack = [person1]
# visited[person1] = True
# break_check = 0

# while True:
#     if stack == []:
#         print(-1)
#         break
    
#     stack_pop = stack.pop()
    
#     if stack == [] and stack_pop != person2:
#         cnt += 1

#     for i in lst[stack_pop]:
#         if visited[i] == False:
#             visited[i] = True
#             stack.append(i)
#         if i == person2:
#             break_check = 1
#             break
    
#     if break_check == 1:
#         if cnt == 0:
#             print(1)
#         else:
#             print(cnt)
#             break
# # [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]
# from collections import deque

# N, M = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(N)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]

# def bfs(a, b):
#     넓이 = 1
#     queue = deque()
#     queue.append((a, b))
#     matrix[a][b] = 0

#     while queue:
#         x, y = queue.popleft()

#         for i in range(4):
#             x_ = dx[i] + x
#             y_ = dy[i] + y

#             if x_ < 0 or x_ >= N or y_ < 0 or y_ >= M:
#                 continue

#             if matrix[x_][y_] == 1:
#                 queue.append((x_, y_))
#                 matrix[x_][y_] = 0
#                 넓이 += 1
#     return 넓이

# cnt = 0
# lst = []
# for i in range(N):
#     for j in range(M):
#         if matrix[i][j] == 1:
#             cnt += 1
#             lst.append(bfs(i, j))
# print(cnt)
# if lst == []:
#     print(0)
# else:
#     print(max(lst))

# N = int(input())
# graph = [list(map(int, input())) for _ in range(N)]


# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def dfs(a, b):
#     lst = [(a, b)]
#     graph[a][b] = 0
#     넓이 = 1
#     while lst:
#         c,d = lst.pop()

#         for i in range(4):
#             x_ = dx[i] + c
#             y_ = dy[i] + d

#             if x_ < 0 or x_ >= N or y_ < 0 or y_ >= N:
#                 continue
#             if graph[x_][y_] == 1:
#                 graph[x_][y_] = 0
#                 lst.append((x_,y_))
#                 넓이 += 1
#     return 넓이

# cnt = 0
# 단지개수 = []
# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == 1:
#             cnt += 1
#             단지개수.append(dfs(i, j))

# print(cnt)
# if 단지개수 == []:
#     print(0)
# else:
#     단지개수.sort()
#     for i in 단지개수:
#         print(i)

# 리스트 비어있을 때 sort쓰면 오류남?
# from collections import deque
# N = int(input())
# person1, person2 = map(int, input().split())
# M = int(input())

# lst = [[] for _ in range(N+1)]
# visited = [False] * (N + 1)
# check_li = [0] * (N + 1)

# for _ in range(M):
#     a, b = map(int, input().split())
#     lst[a].append(b)
#     lst[b].append(a)


# def bfs(a):
#     queue = deque()
#     queue.append(a)
#     visited[a] = True
    
#     while queue:
#         pop_num = queue.popleft()

#         for i in lst[pop_num]:
#             if visited[i] == False:
#                 queue.append(i)
#                 check_li[i] = check_li[pop_num] + 1 # 노드로 생각하면 된다 본인 노드에있는 데이터는 1촌 다음 이어진 노드 데이터들은 모두 2촌 그다음은 3촌.....이렇게 쭉 카운트한다
#                 visited[i] = True
# bfs(person1)
# if check_li[person2] == 0:
#     print(-1)
# else:
#     print(check_li[person2])

# from collections import deque
# import sys

# M, N = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]
# queue = deque()

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def bfs():
#     while queue:
#         x, y = queue.popleft()
        
#         for a in range(4):
#             x_ = dx[a] + x
#             y_ = dy[a] + y
            
#             if x_ < 0 or x_ >= N or y_ < 0 or y_ >= M:
#                 continue
            
#             if graph[x_][y_] == 0:
#                 graph[x_][y_] = 1 + graph[x][y]
#                 queue.append((x_, y_))



# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 1:
#             queue.append((i, j))
            
# bfs()
# li = []
# for i in graph:
#     li.append(max(i))
#     for j in i:
#         if j == 0:
#             print(-1)
#             sys.exit(0)
# print(max(li) - 1)

# from collections import deque
# m, n, h = map(int, input().split())

# main_lst = [[] for _ in range(h)] 

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# dz = [1,-1]

# # 그래프로 받은 1차원리스트를 main_lst(2차원 비어있는 리스트)에 담아 최종적으로 3차원 리스트의 형태로 만든다
# for i in range(h):
#     for _ in range(n):
#         main_lst[i].append(list(map(int, input().split())))

# # 만약 main_lst에 1이 여러개인 경우 가장 짧은 일수를 구해야하기 때문에 여러개의 1을 동시에 일수를 계산하며 함수를 동작시켜야한다
# # 그래서 1에 해당하는 인덱스를 다 담아놓고 시작해야 하기 때문에 함수 밖으로 빼서 append하고 append가 다 끝나면
# # 함수를 동작시켜서 덱 자료구조로 실행하면 차근차근 1부터 계산해나가기 때문에 가장 짧은 일수를 구할 수 있다 
# queue = deque()

# def bfs():
#     while queue:
#         z, x, y = queue.popleft()

#         # 앞, 뒤만 따로 먼저 out of range, 0여부를 검사한다 x, y는 popleft한 고정값을 사용하면 된다
#         for b in range(2):
#             z_ = dz[b] + z

#             if z_ < 0 or z_ >= h:
#                 continue
#             if main_lst[z_][x][y] == 0:
#                 main_lst[z_][x][y] = main_lst[z][x][y] + 1
#                 queue.append((z_, x, y))

#         # 앞 뒤를 검사한뒤 popleft한 값에서 x, y의 상하좌우를 검사한다
#         for a in range(4):
#             x_ = dx[a] + x
#             y_ = dy[a] + y

#             if x_ < 0 or x_ >= n or y_ < 0 or y_ >= m: # 본인이 밖으로 나가는 경우
#                 continue
            
#             if main_lst[z][x_][y_] == 0:
#                 main_lst[z][x_][y_] = main_lst[z][x][y] + 1
#                 queue.append((z,x_,y_))

# # 3중 for문을 돌면서 1을 발견하면 인덱스 값을 덱에 다 넣는다
# for i in range(h):
#     for j in range(n):
#         for k in range(m):
#             if main_lst[i][j][k] == 1:
#                 queue.append((i,j,k))
# bfs()

# # 다 완성된 main_lst를 순회하면서 0이 있으면 -1을 출력하고 프로그램 종료, 아니라면 가장 큰 값을 변수에 담는다다
# res = 0
# for i in main_lst:
#     for j in i:
#         if 0 in j:
#             print(-1)
#             exit(0)
#         if max(j) > res:
#             res = max(j)
# print(res - 1) # 처음 본인 일수는 빼야한다

# from collections import deque
# T = int(input())

# for t in range(T):
#     n = int(input())
#     chess = [[0] * n for _ in range(n)]

#     kni, ght = map(int, input().split())
#     desti, nation = map(int, input().split())

#     # +1,+2 -1+2 +1,-2 -1,-2 +2,+1 +2,-1 -2,+1 -2,-1 나이트의 이동 경로 8방향
#     search = [(1,2), (-1,2), (1,-2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]

#     def bfs(kni, ght):
#         queue = deque()
#         queue.append((kni, ght))
#         chess[kni][ght] = 1

#         while True:
#             x, y = queue.popleft()

#             for i in search:
#                 x_ = i[0] + x
#                 y_ = i[1] + y

#                 if x_ < 0 or x_ >= n or y_ < 0 or y_ >= n:
#                     continue

#                 if chess[x_][y_] == 0:
#                     chess[x_][y_] = chess[x][y] + 1
#                     queue.append((x_,y_))
            
#             if x == desti and y == nation:
#                 break
#     bfs(kni, ght)

#     print(chess[desti][nation] - 1)

# from collections import deque
# n, k = map(int, input().split())
# visited = [0] * 100001

# cnt = 0 
# def bfs(n, k):
#     global cnt
#     queue = deque()
#     queue.append(n)
#     visited[n] = 1
    
#     while queue:
#         cur = queue.popleft()
#         if cur == k:
#             cnt += 1 

#         for i in (cur-1, cur+1, cur*2): # bfs문제는 이렇게 현재위치에서 이동하는 위치를 어떻게 잘 지정해서 구하느냐의 문제인 것 같다

#             if i < 0 or i >= 100001:
#                 continue

#             if visited[i] == 0 or visited[cur] + 1 == visited[i]: # 처음 i가 k와 같다면 k는 0이라 최단거리로 바꿔준다
#                 visited[i] = visited[cur] + 1                       # 같은 최단거리에서 k가 되는 i도 append하게 만들어줘야한다
#                 queue.append(i)                                     # 그래서 조건을 현재위치에서 +1한 값과 바뀌는 값인 i가 같다면 append하게 만들어준다
# bfs(n, k)                                                           # 그럼 최단거리+1이상부터 i가 k와 같아도 append되지 않는다
# print(visited[k] -1)
# print(cnt)
# 
# T = int(input())
# for _ in range(T):

# import time
# start = time.time()

# k = int(input())
# n = int(input())

# def f(k, n):
#     if n == 1: # 호수가 1이면 사람수는 무조건 1명이다
#         return 1 
#     if k == 0: # 0층의 사람수는 호수와 같다 0층 3호면 3명이 있다 n을 리턴한다
#         return n
#     return f(k-1, n) + f(k, n-1) # 최종적으로 구하고자하는 층수와 호수에서 각각 1씩 뺀 사람수가 정답
# print(f(k, n))

# end = time.time()
# print(end-start)

# 피보나치 DP 재귀, 메모이제이션, 바텀업

# 재귀
# import time
# start = time.time()
# def fibo(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     return fibo(n-1) + fibo(n-2)
# print(fibo(15))
# end = time.time()
# print(end-start)

# 메모이제이션 시간이 매우 단축되었다다
# import time
# start = time.time()
# dp = [0] * 100

# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     if dp[n] != 0: # 갱신된 값이 0이 아니니까 갱신된 값을 리턴한다 굳이 함수를 호출 하지않아도 된다
#         return dp[n]
#     dp[n] = fibo(n-1) + fibo(n-2) # dp라는 리스트에 조건식이 해당하지 않는 경우 값을 넣어줘야함
#     return dp[n]

# print(fibo(99))

# end = time.time()
# print(end-start)

# 하지만 함수의 깊이가 많이 깊어지게 되면 리커전에러가 발생한다 그때 사용하는 것
# 바텀업 (반복문으로 해결) 작은 답에서 큰 답으로 아래에서 위로 올라가면서 답을 구한다
# import time
# start = time.time()

# dp = [0] * 100 # 리스트를 생성하는 것은 같다
# dp[1] = 1
# dp[2] = 1
# n = 99

# for i in range(3, n+1):
#     dp[i] = dp[i-1] + dp[i-2]

# print(dp[n])

# end = time.time()
# print(end-start)
# import math
# n = int(input())
# n_list = list(map(int, input().split()))
# cnt = 0

# def primeNumber(k):                         # 소수가 아닌 약수의 특성상 가운데 약수를 기준으로 곱셈연산이 대칭을 이룬다
#     for j in range(2, int(math.sqrt(k))+1): # math모듈의 sqrt함수 인자값에 루트를 씌운다
#         if k % j == 0:                      # 예를 들어 16이면 1 2 4 8 16 인데 이중 제곱근인 4까지만 봐도 소수인지 아닌지 알 수 있다
#                                             # 쓰는 이유
#             return False                    # 만약 반복문도는 숫자가 소수로 입력받은 경우 중간 리턴이 발생하지않고 첨부터 끝까지 다 봐야하기 때문에
#     return True                             # 소수인 수를 고려해서 시간복잡도를 줄이는 방법이다
#                                             # 즉 소수가 들어와도 11이라면 루트11 + 1 까지만 확인해봐도 소수인지 아닌지 알수가있다
# for i in n_list:
#     if i == 1:
#         continue
#     if i == 2:
#         cnt += 1
#     else:
#         if primeNumber(i):
#             cnt += 1
# print(cnt)
# import math

# T = int(input())
# for _ in range(T):
#     n = int(input())
#     prime = [True for _ in range(n+1)] # 에라토스테네스의 체 
#     prime[0] = False                    # 2부터 특정 수 n까지 총 소수가 몇개인지??구한다
#     prime[1] = False                    # True가 n+1개 들어간 리스트생성 
#                                         # 2부터 sqrt(n)+1까지 소수인 수를 찾고 소수면 그 수의 배수를 전부 False처리한다(배수라는 얘기는 약수임)
#     for i in range(2, int(math.sqrt(n))+1): # 리스트에 남은 True의 ?번째 수들은 모두 소수이다 2번째 수가 True면 2가 소수라는 얘기
#         if prime[i] == True:
#             multi = 2
#             while n >= multi * i:
#                 prime[i * multi] = False
#                 multi += 1
#     lst = []
#     for i in range(1, n+1):
#         if prime[i]:
#             lst.append(i)
#     lst2 = []
#     gap = 10000
#     result = 1
#     for i in lst:
#         for j in lst:
#             if i + j == n:
#                 if i <= j:
#                     if gap > j - i:
#                         gap = j - i
#                         result = i, j
#     print(*result)

# 입력받은 2차원리스트 전체순회한번 해야됨 전체가 1장 조건만족할 수도있다
# 전체가 한장이 아니라면 총 9장으로 잘라야됨
# 최종적으로 리턴 받는 값은 현재 들어온 2차원 리스트가 종이가 몇개인지 
# 쪼갤 필요가없으면 바로 1장으로 리턴해야됨
# 쪼개야하면 쪼개서 함수 호출 해야됨

# import math
# T = int(input())
# for _ in range(T):

#     n = int(input())
#     li = [True for _ in range(n+1)]
#     lst = [i for i in range(n+1)]
#     li[0] = False
#     li[1] = False

#     for a in range(2, int(math.sqrt(n))+1):
#             if li[a] == True:
#                 cnt = 2

#                 while a * cnt <= n:
#                     li[a * cnt] = False
#                     cnt += 1

#     # add = 0
#     # for i in range(2, len(li)):
#     #     for j in range(2, len(li)):
            
#     #         if li[i] == True and li[j] == True:
#     #             if i >= j:
#     #                 if i + j == n:
#     #                     add += 1
#     # print(add)

# n = int(input())
# li = [int(input()) for _ in range(n)]

# check_3 = 0
# score = 0
# # n-2의 인덱스라면 점수 더하고 바로 종료
# for i in range(n-1):
#     if check_3 < 3:
#         score += li[i]
#         check_3 += 1
#         if i == n-3:
#             break
#     else:
#         check_3 = 1
#         continue
# print(li[-1] + score)

# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]

# # 3경우를 다 보고, 모든 경로를 다 탐색한다 최종적으로 가장 작기만 하고 조건에 부합하면 그만이다
# for i in range(1, n):
#     graph[i][0] = min(graph[i - 1][1], graph[i - 1][2]) + graph[i][0]

#     graph[i][1] = min(graph[i - 1][0], graph[i - 1][2]) + graph[i][1]

#     graph[i][2] = min(graph[i - 1][1], graph[i - 1][0]) + graph[i][2]
# print(min(graph[n-1])) # 가장 마지막에서 가장 작은 수를 골라내는게 핵심인 것

# n = int(input())

# stair = []
# for _ in range(n):
#     stair.append(int(input()))

# if n < 3:
#     print(sum(stair))
#     exit()

# dp = [] # 값이 가장 큰 최적의 값을 저장한다

# dp.append(stair[0])
# dp.append(stair[0] + stair[1])
# dp.append(max(stair[0] + stair[2], stair[1] + stair[2]))

# for i in range(3, n):
#     case1 = stair[i] + dp[i-2]
#     case2 = stair[i] + stair[i-1] + dp[i-3] # 여기서 stair[i-1]을 한 이유는 i가 3일 때 dp[2]를 더해버리면 앞에서 stair[1]+stair[2]로 초기화된
#     dp.append(max(case1, case2))            # 값이 들어있다면 1+2+3의 인덱스값이 더해지기 때문에 조건에 맞지 않게된다
#                                             # [i-1], [i-3]을 구할 땐 가중치가 들어오지 않은 경우를 봐야하므로 그냥 stair[i-1]을 넣는다
#                                             # 나머지 경우는 한칸 띄어져있기 때문에 가중치가 들어와야한다 (값이 가장 큰 최적의 경로)
#                                             # 그 앞에서 구한 값이 가장 최적의 값이기 때문
# print(dp[n-1])

# for i in range(3,3): # 동작만 하지않을 뿐, 에러가 나진 않는다
#     print(1)

# dp(최대비용) = [0, 1, 2의최대비용, 3의최대비용, ...]
n = int(input())
li = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + li[j]) # 각 dp인덱스별 최대비용 + 그냥비용리스트
print(dp[n])                                   # n이 3이라면 dp[3]을 구할 때 2의최대비용+1의비용, 1의최대비용+2비용, 0의최대비용+3의비용을 구하게된다 