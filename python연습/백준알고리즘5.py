# 삼각형 외우기(10101)
# a = int(input())
# b = int(input())
# c = int(input())
# if a + b + c != 180:
#     print('Error')
# elif a == 60 and b == 60 and c == 60:
#     print("Equilateral")
# else:
#     if a == b or a == c or b == c:
#         print("Isosceles")
#     else:
#         print("Scalene")

# # 세탁소 사장 동혁(2720)
# T = int(input())
# for t in range(T):
#     coin = int(input()) 
#     lst = []
#     a = coin // 25
#     b = (coin - 25 * a) // 10
#     c = ((coin - 25 * a) % 10) // 5
#     d = ((coin - 25 * a) % 10) % 5 
#     lst.append(a)
#     lst.append(b)
#     lst.append(c)
#     lst.append(d)
#     print(*lst)

# # 피시방 알바(1453)
# from collections import deque
# N = int(input())
# count = 0
# cus = deque(map(int,input().split()))
# first_cus = []
# while True:
#     try:
#         if cus[0] in first_cus:
#             count += 1
#         first_cus.append(cus.popleft())
#     except:
#         break
# print(count)

# # 제로(10773)
# N = int(input())
# arr = []
# for i in range(N):
#     num = int(input())
#     if num != 0:
#         arr.append(num)
#     else:
#         arr.pop()
# print(sum(arr))

# # 카드1(2161)
# from collections import deque
# N = int(input())
# lst = deque(range(1, 1+N))
# em_lst = []
# while len(lst) != 1:
#     em_lst.append(lst.popleft())
#     lst.append(lst.popleft())
# print(*em_lst, *lst)

# 괄호(9012)
# 만약 (라면 리스트에 append
# 만약 lst가 비어있는데 )이게 들어오면 NO 
# N = int(input())
# for _ in range(N):
#     string = input()
#     a = 0
#     lst = []
#     for i in string:
#         if i == '(':
#             lst.append(i)
#         else:
#             try:
#                 lst.pop() 
#             except:
#                 a = 1
#     if a == 1: 
#         print('NO')
#     elif lst == []:
#         print('YES')
#     else:
#         print('NO')