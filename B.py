#B
import sys
sys.setrecursionlimit(int(1e6))
sum,lc,cnt=0,1,0
for i in range(1,10001):
    sum+=i
    lc*=i
    if (sum-lc)%100==0:
        print(i)
        cnt+=1
    if i%200==0:
        print(i,cnt)
        cnt=0
print(2+2024041331404202//200*4)
'''
40480826628086
'''