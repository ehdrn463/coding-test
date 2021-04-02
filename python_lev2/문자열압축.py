def solution(s):
    # 단위: scale
    total = list()
    # 단위 가능한 숫자 문자열이 한개 인 경우 len(s)//2 +1 하면 1돼서 런타임 에러 발생함
    for i in range(1, len(s)//2+2):
        scale = i
        new_zip = list()
        # 단위에 맞게 잘려진 문자열 더하기
        for j in range((len(s) // scale)+1):
            new_zip.append(s[j*scale:j*scale+scale])
    
        cnt_new_zip = ''
        
        temp = 1
        # 하나씩 비교하면서 압축가능한 문자열 체크하기
        while (new_zip):
            fst = new_zip.pop(0)
            if len(new_zip) == 0:
                cnt_new_zip += fst
            elif fst == new_zip[0]:
                temp += 1
            else:
                if temp == 1:
                    cnt_new_zip += fst
                else:
                    cnt_new_zip += str(temp) + fst
                temp = 1
        if len(total) == 0:
            total.append([i, cnt_new_zip])
        else:
            if len(total[0][1]) > len(cnt_new_zip):
                total[0] = [i, cnt_new_zip]

    return len(total[0][1])


solution("abcabcabcabcdededededede")