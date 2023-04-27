# 오븐시계(2525)
H, M = map(int, input().split())
mi = int(input())
if mi + M < 60:
    M = mi + M
else:
    H = H + ((mi + M) // 60)
    M = (mi + M) % 60

if H > 23:
    H = H % 24
print(H, M)

# 블랙잭(2798)
# 567 568 569 578 579 589 678 679 789
card_n, b_j = map(int, input().split())
cards = list(map(int, input().split()))
lst = []
for i in range(card_n-2): # 3장을 이용한 문제기 때문에 뒤에 2장을 순회하지 않는다 -2
    for j in range(i+1, card_n-1): # 여긴 1장 앞에서 출발, 뒤 1장을 순회하지 않는다
        for q in range(j+1, card_n): # 앞에 2장을 순회하지않고 맨 뒤까지 순회한다
            total = cards[i] + cards[j] + cards[q]
            if total <= b_j:
                lst.append(total)
print(max(lst))

# 점수집계(9076)
T = int(input())
for _ in range(T):
    scores = list(map(int, input().split()))
    scores.sort()
    scores.pop()
    scores.pop(0)
    if scores[-1] - scores[0] >= 4:
        print('KIN')
    else:
        print(sum(scores))

# 가장 큰 금민수(1526)
N = int(input()) 
N = list(map(str, range(N+1)))
blank = []
for i in ['0','1','2','3','5','6','8','9']:
    for j in N:
        if i in j:
            blank.append(int(j)) # N중에 하나라도 들어있으면 blank로 집어넣음
N = list(map(int, N))
N = set(N)
blank = set(blank)
minsu_li = list(N - blank) # 차집합이용함 그럼 4, 7로 이루어진 숫자만 남음
minsu_li.sort() # 정렬
print(minsu_li[-1]) # 가장큰 수

# 영화감독 숌(1436)
N = int(input())
lst = []
a = 0
while len(lst) != N:
    a = a + 1
    if '666' in str(a):
        lst.append(a)
print(lst[-1])


