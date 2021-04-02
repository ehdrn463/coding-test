def calc_axis(drawing_line, x, y):
    # 아래로 내려가는 경우 (x+=1)
    if drawing_line % 3== 0:
        x+=1
    # 오른쪽으로 한 칸씩 가는 경우(y+=1)
    elif drawing_line % 3== 1:
        y+=1
    # 위로 가는 경우(x-=1, y-=1)
    else:
        x-=1; y-=1
    return x,y

def solution(n):
    answer = [[0]*(i+1) for i in range(n)]
    adding_num = 0

    # 한줄 쫙 긋는 경우 n개로 시작
    # 그 다음 n-1개, 그 다음 n-2개 .... 1개까지
    drawing_cnt = n

    # 줄 그은 갯수 drawing_line
    # 나머지 0: 내려간다
    # 나머지 1: 오르쪽으로 간다
    # 나머지 2: 위로 올라간다.
    drawing_line = 0
    x,y = -1, 0
    while drawing_cnt >=1:
        for i in range(drawing_cnt):
            adding_num +=1
            x, y = calc_axis(drawing_line, x, y)
            answer[x][y] = adding_num
        drawing_line +=1
        drawing_cnt -=1
    print(answer)
    result = []
    for a in answer:
        result+=a
    return result


solution(4) #[1,2,9,3,10,8,4,5,6,7]
solution(5) #[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
solution(6) #[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]

