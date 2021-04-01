def solution(s):
    # 단위: scale
    total = list()
    for i in range(1, len(s)//2+2):
        scale = i
        new_zip = list()
        for j in range((len(s) // scale)+1):
            new_zip.append(s[j*scale:j*scale+scale])
    
        temp = 1
        cnt_new_zip = ''
        
        temp = 1
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