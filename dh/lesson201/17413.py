import sys
S = list(sys.stdin.readline().strip().split(">"))
for i in range(len(S)):
    here = list(S[i])
    if here == []: pass
    elif here[0]=="<": # <로 시작하는 경우 태그임
        S[i] = S[i] + ">" 
    else:
        if S[i].find("<") == -1: # 안에 <가 없는 경우
            part = S[i].split(" ") # 공백을 기준으로 나누고
            for j in range(len(part)):
                word = list(part[j]) # 나뉜 단어를 분할한 뒤
                word.reverse() # 순서를 역전시키고
                word = ''.join(word) # 다시 합쳐서
                part[j] = word  # 원래 자리에 대입
            S[i] = ' '.join(part) # 나눈 단어를 공백 기준으로 합쳐서 원래 자리에 대입
            
        else: # 안에 <가 있는 경우
            words = S[i].split("<") # <를 기준으로 나누고
            part = words[0].split(" ") # 순서를 뒤집을 단어를 공백 기준 분리
            for j in range(len(part)): # 위와 동일하게 진행 
                word = list(part[j])
                word.reverse()
                word = ''.join(word)
                part[j] = word
            words[0] = ' '.join(part) # 처리한 단어를 다시 공백 기준 병합
            S[i] = '<'.join(words) + ">"
print(''.join(S))