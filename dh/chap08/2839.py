from xml.dom.expatbuilder import FilterVisibilityController


N = int(input())
fives = 1001
threes = 2000
for i in range(N//5, -1, -1):
    left = N-i*5
    if left%3==0 and (i+left//3)<(fives+threes): 
        fives = i; threes = left//3
if fives==1001 and threes==2000: print(-1)
else: print(fives+threes)