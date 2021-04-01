import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []
    
    # 처리한 갯수가 len(jos) 보다 작을 때까지 반복.
    while i < len(jobs):
        # jobs의 요청시간을 보면서 처리할 수 있는 것을 더해준다.
        for j in jobs:
            # 요청시간이 이전 작업의 완료시간보다 크고, 현재시간보다 작거나 같다면 처리해줄 수 있는 작업임
            # 요청시간(j[0]) 기준으로 더 빠른 놈을 heap에다 추가한다.
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        # 만약 처리할 놈이 있으면
        if len(heap)> 0:
            print(len(heap), '처리할 놈이 있다')
            # 제일 먼젓놈을 빼주고
            current = heapq.heappop(heap)
            # 시작지점을 현재시간으로 설정해주고
            start = now
            # 현재시간에다 소요시간을 더해준다
            now += current[0]
            # 누적시간에는 작업이 마무리된 시점에서 요청된 시점을 빼서 더한다.
            answer += (now-current[1])
            i +=1
            print('1 더 했다.')
        else:
            # 처리해줄 놈이 없으니 현재시간을 1 늘려준다.
            now += 1
    print(int(answer / len(jobs)))
    return int(answer / len(jobs))

# solution([[0, 3], [1, 9], [2, 6]])
solution([[0, 3], [1, 9], [2, 6], [30, 3]])