# 평균점수(10039)
all_score = 0
for i in range(5):
    score = int(input())
    if score < 40:
        score = 40
    all_score += score
print(all_score//5)

# X보다작은수(10871)
n, x = map(int,input().split())
a = list(map(int,input().split()))
for i in a:
    if i < x:
        print(i,end=" ")

# 주사위세개(2480)
a, b, c = list(map(int,input().split()))
num_list = [a, b, c]
if a == b and a == c:
    money = 10000 + a * 1000
elif a == b or b == c:
    money = 1000 + b * 100
elif a == c:
    money = 1000 + a * 100
else:
    num_list.sort()
    money = num_list[-1] * 100
print(money)

# 0 = not cute / 1 = cute(10886)
T = int(input())
not_cute = 0
cute = 0
for t in range(1,1+T):
    vote = int(input())
    if vote == 1:
        cute += 1
    else:
        not_cute += 1
if not_cute > cute:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")

# 점수계산(2506)
T = int(input())
zoro = list(map(int,input().split()))
count_list = []

for t in range(T):
    if zoro[t] == 0:
        count_list.append(0)
    else:
        if t == 0:
            count_list.append(1)
        elif zoro[t-1] == 0:
            count_list.append(1)
        else:
            count_list.append(count_list[t-1] + 1)
print(sum(count_list))
