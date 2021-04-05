# txt => '균형잡힌 괄호 문자열'u & '균형잡힌 괄호 문자열'v
def splash(txt):
    if txt == '':
        return ''
    temp = ''
    for i in range(len(txt)):
        temp = txt[:i+1]
        left_cnt = temp.count('(')
        right_cnt = temp.count(')')
        if (left_cnt == right_cnt):
            u = temp; v = txt[i+1:]
            return (u,v)
# print(splash("()))((()"))


# 올바른 괄호 문자열 체크
def check_right(txt):
    u, v = splash(txt)
    for i in range(len(u)//2+1):
        j = len(u) - i


print(check_right("(()())()")) 

def solution(p):
    answer = ''
    return answer


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"	))