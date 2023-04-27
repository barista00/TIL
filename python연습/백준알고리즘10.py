# 공(1547)
# lst = ['ball','X','X'] # ball position
# M = int(input())

# for m in range(M):
#     x, y = map(int, input().split())
#     lst[x-1], lst[y-1] = lst[y-1], lst[x-1]

# print(lst.index('ball')+1)

# 콘테스트(5576)
# W = []
# for i in range(10):
#     score = int(input())
#     W.append(score)
# K = []
# for i in range(10):
#     score = int(input())
#     K.append(score)
# W.sort()
# K.sort()

# W_Top = 0
# K_Top = 0
# for i in range(1,4):
#     W_Top += W[-i]
#     K_Top += K[-i]

# print(W_Top, K_Top)

# 오르막길(2846)
N = int(input())
road = list(map(int, input().split()))
# 리스트에 데이터를 i-1, i 두개씩 비교하면서 오르막길인지 확인
max_length = 0
start = 0
end = 0 
for i in range(1,N):
    if road[i] > road[i-1]:

        if start == 0:
            start = road[i-1] # 오르막길일 때 start값 할당함
        
        
        if i == N-1: # 처음부터 끝까지 오르막길일 때 end값 할당
            end = road[i]
            length = end - start
            if max_length < length:
                max_length = length
    
    elif road[i] <= road[i-1]: # 오르막길로 가다가 아닌상황일 때 앞 오르막길의 end값 할당
        if start != 0: # 오르막길이 시작한건지 여부 확인
            end = road[i-1]
            length = end - start # 오르막길이 끝나게 되는경우 오르막길 높이 갱신
            if max_length < length:
                max_length = length
            start = 0
print(max_length)
# 변수들을 활용해서 값을 비교하고 할당하고를 하며 로직을 짜는게 핵심인 문제같다
# 앞으로 문제풀 때 변수를 어떻게 활용하는지 먼저 생각해보아야 할 것 같다

# 단어 나누기(1251)
# N = input()
# # 단어 입력받기

# # 총 2번에 나눠서 3덩이리로 자른다
# # a/b/ccc
# # 아무리 적어도 최소 1개 알파벳으로 잘라야함 시작은 1까지
# # 두번째는 앞에서 +1이 최소 슬라이스 그리고 맨마지막에서 앞에까지
# lst = []
# length = len(N)
# # 맨앞에 슬라이싱을 위한 반복문
# for i in range(1,length-1):
#     # 두번째 슬라이싱을 위한 반복문
#     for j in range(i+1, length):
#         f = N[:i] # 맨앞부분
#         s = N[i:j] # 두번째 부분
#         t = N[j:] # 세번째 부분

#         lst.append(f[::-1]+s[::-1]+t[::-1]) # 슬라이싱한 단어를 역순으로 정렬후 합치기
# print(min(lst)) # 사전순에서 가장 앞에 나오는 단어출력





