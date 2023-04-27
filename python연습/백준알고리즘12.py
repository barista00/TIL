# 막대기(17608)
# N = int(input())

# lst = []
# for _ in range(N):
#     stick = int(input())
#     lst.append(stick)

# cnt = 1
# master = lst[-1]
# for i in reversed(range(N)):
#     if lst[i] > master:
#         cnt += 1
#         master = lst[i]
# print(cnt)

# 덩치(7568)
# N = int(input())

# lst = []
# for i in range(N):
#     WandH = list(map(int, input().split()))
#     lst.append(WandH)

# grade_li = []
# compare = 0

# while compare != N :
#     grade = 1
#     for i in range(N):
#         if lst[compare][0] < lst[i][0] and lst[compare][1] < lst[i][1]:
#             grade += 1
#     grade_li.append(grade)
#     compare += 1
# print(*grade_li)

# 킹(1063)
import pprint
board = [[False]*10 for _ in range(10)] # 10X10 의 False로 이루어진 2차원 리스트 형성
# pprint.pprint(board)

for i in range(1,9): # 1~8까지 'T'로 바꿔주면 False로 둘러싸인 8X8체스판 완성
    for j in range(1,9):
        board[i][j] = 'T' # 0으로 설정 했을 때 False랑 같냐라는 if문에서 문제가 발생했음 0은 함부로 사용하면 안됨
# pprint.pprint(board)

K, R, N = map(str, input().split())
kx, ky = ord(K[0])-64, 9-int(K[1]) # 열은 아스키코드로 변환 행은 9에서 빼준 값
rx, ry = ord(R[0])-64, 9-int(R[1]) 
board[ky][kx] = 'King'
board[ry][rx] = 'Rock'

# pprint.pprint(board)

move = { # 움직일 좌표
    'R' : (0,1),
    'L' : (0,-1),
    'T' : (-1,0),
    'B' : (1,0),
    'RT': (-1,1),
    'LT': (-1,-1),
    'RB': (1,1),
    'LB': (1,-1)
}

for i in range(int(N)): # 체스판에서 킹, 돌맹이를 인풋에 맞게 옮겨준다(굳이 안옮겨도 되는데 그냥 해봄)
    position = input()
    if board[ky + move[position][0]][kx + move[position][1]] != False: # 킹 기준 움직여야하는 위치가 False가 아니면
        # print(1)
        if board[ky + move[position][0]][kx + move[position][1]] == 'Rock': # 킹 기준 움직여야하는 위치에 Rock이 있다? 
            if board[ry + move[position][0]][rx + move[position][1]] == False: # 킹의 움직이는 위치가 Rock이고 밀려난 Rock이 False라면
                pass
            else:
                board[ry][rx] = 'T'
                ry, rx = ry + move[position][0], rx + move[position][1]
                board[ry][rx] = 'Rock' # Rock위치에서 인풋 값만큼 Rock위치 조정
                
                board[ky][kx] = 'T'
                ky, kx = ky + move[position][0], kx + move[position][1]
                board[ky][kx] = 'King' # 킹 위치에서 인풋 값만큼 킹 위치 조정
        else: # 킹이 움직이는 위치에 Rock이 걸리지 않는 경우
            board[ky][kx] = 'T'
            ky, kx = ky + move[position][0], kx + move[position][1]
            board[ky][kx] = 'King'

print(chr(kx + 64) + str(9 - ky)) # 최종 킹의 위치(열)를 다시 문자로 바꾸고 행의 크기에서 9를 뺀 값과 더한다  
print(chr(rx + 64) + str(9 - ry)) # 최종 Rock의 위치 다시 문자로 바꾸고 행의 크기에서 9를 뺀 값과 더한다
# pprint.pprint(board)

