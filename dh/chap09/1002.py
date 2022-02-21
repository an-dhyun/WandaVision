T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    r_dist = r1+r2
    c_dist = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    
    if r_dist == c_dist: print(1)
    elif r_dist < c_dist: print(0)
    elif r_dist > c_dist: 
        if c_dist == 0: 
            if r1 == r2: print(-1)
            else: print(0)
        else: print(2)