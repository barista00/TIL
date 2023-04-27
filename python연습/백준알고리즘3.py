# 시험성적(9498)
score = int(input())
if score >= 90:
    print('A')
elif 80 <= score < 90:
    print('B')
elif 70 <= score < 80:
    print('C')
elif 60 <= score < 70:
    print('D')
else:
    print('F')

# 단어 뒤집기(9093)
T = int(input())
for t in range(1, 1+T):
    sen = input().split()
    for i in sen:
        print(i[::-1], end=" ")
    print('')

# 열개씩 끊어 출력하기(11721)
sen = input()
a = 0
for i in sen:
    if a > 9:
        print('')
        print(i,end="")
        a = 1
    else:
        print(i,end="")
        a += 1

# 나무조각(2947)
nums = list(map(int,input().split()))

while True:
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i] # 데이터 스와핑
            for j in nums:
                print(j,end=" ")
            print('')
    if [1,2,3,4,5] == nums:
        break
    
