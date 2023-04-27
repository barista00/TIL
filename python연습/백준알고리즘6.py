# 세 수(10817)
# import heapq
# number3 = list(map(int,input().split()))
# heapq.heapify(number3)
# heapq.heappop(number3)
# print(number3[0])

# 고무오리 디버깅(20001)
# 고무오리 디버깅 끝 나오면 인풋 중지
# 리스트에 문제라는 단어가 없는데 고무오리가 들어오면 문제둘 추가
# N = input()
# lst = []
# while True:
#     problem = input()
#     if problem == '고무오리 디버깅 끝':
#         break
#     else:
#         if problem == '문제':
#             lst.append(problem)
#         else:                       # 고무오리 들어온경우
#             if '문제' not in lst:  # 문제가 없는데 고무오리가 들어온 경우
#                 lst.append('문제')
#                 lst.append('문제')
#             else:                   # 문제 있는데 고무오리 들어온 경우
#                 lst.pop()
# if '문제' in lst:
#     print('힝구')
# else:
#     print('고무오리야 사랑해')

# 대칭 차집합(1269)
# a, b = map(int, input().split())
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# A = set(A)
# B = set(B)
# print(len(A-B)+len(B-A))

# 나머지(3052)
# lst = []
# for i in range(10):
#     num = int(input())
#     lst.append(num % 42)
# set_lst = set(lst)
# print(len(set_lst))

# 단어정렬(1181)
# 가장 먼저 단어개수 순으로 정렬하는데 만약 단어수가 같다면 사전순으로 정렬
N = int(input())
lst = []
for _ in range(N):
    alpha = input()
    lst.append(alpha)   # lst에 인풋 다 집어넣기
lst = set(lst)  # 똑같은 데이터 하나로 만들기
lst = list(lst)     # 다시 리스트로 바꾸기
lst.sort(key=len)   # 길이순으로 정렬
for i in range(len(lst)-1):
    if len(lst[i]) == len(lst[i+1]):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]     # 길이가 같은 경우 알파벳순 정렬
for i in lst:
    print(i)

# 절댓값 힙(11286)
# 배열에 정수 x를 넣는다
# 0보다 작은 경우 : (N*-1, -1)
# 0보다 큰 경우 : (N, 0)
# import heapq
# import sys
# N = int(sys.stdin.readline())
# arr = []
# heapq.heapify(arr)
# for n in range(N):
#     num = int(sys.stdin.readline())
#     if num < 0:
#         heapq.heappush(arr, (num*-1, -1))
#     elif num > 0:
#         heapq.heappush(arr, (num, 0))
#     else: # 0이 들어온 경우
#         if arr == []:   # arr에 아무것도 없음
#             print(0)
#         else:       # arr에 뭐가 들어있음
#             if arr[0][1] == -1: # 맨앞의 튜플이 음수인 경우
#                 print(arr[0][0]*arr[0][1])
#                 heapq.heappop(arr)
#             else:   # 양수인 경우
#                 print(arr[0][0])
#                 heapq.heappop(arr)
# # 11286 코드 조정
# import heapq
# import sys
# N = int(sys.stdin.readline())
# arr = []
# for _ in range(N):
#     num = int(sys.stdin.readline())
#     if num:
#         heapq.heappush(arr, (abs(num), num))
#     else: # 0이 들어온 경우
#         if arr == []:   # arr에 아무것도 없음
#             print(0)
#         else:       # arr에 뭐가 들어있음
#             print(heapq.heappop(arr)[1])