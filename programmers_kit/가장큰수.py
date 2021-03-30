from functools import cmp_to_key

# 오름차순으로 정리
# 앞자리가 클 수록 앞으로.
# 사전 순으로 하면 뒤에 나오는게 앞으로
def compare(a,b):
    if a+b > b+a:
        return -1
    else:
        return 1

def solution(numbers):
    numbers = [str(n) for n in numbers]
    numbers = sorted(numbers, key=cmp_to_key(compare))
    print(''.join(numbers))
    return 0 or ''.join(numbers)
solution([6,10,2])
solution([3,30,34,5,9])
solution([3,30,34,5,99,999])