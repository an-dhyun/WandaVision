while True:
    a, b, c = map(int, input().split())
    lens = [a, b, c]
    if sum(lens)==0: break
    max_len = max(lens)
    lens.remove(max_len)
    if max_len**2 == lens[0]**2 + lens[1]**2 : print('right')
    else: print('wrong')