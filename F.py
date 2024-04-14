#F
import sys
sys.setrecursionlimit(int(1e6))

n=int(1e5)
isPrime=[1]*int(1e5+10)
prime=[]
isPrime[1]=0
for i in range(2,n+1):
    if isPrime[i]:prime.append(i)
    for j in prime:
        if i*j>n:break
        isPrime[i*j]=0
        if i%j==0:break

win=[0]*int(1e5+10)
def dfs(x):
    if x<=1:return 0
    if win[x]==1:return 1
    if win[x]==-1:return 0
    if isPrime[x] or isPrime[x-1]:
        win[x]=1
        return 1
    for i in prime:
        if i>x:break
        if not dfs(x-i):
            win[x]=1
            return 1
    win[x]=-1
    return 0

T=int(input())
a=[]
for _ in range(T):
    print(dfs(int(input())))
'''
3
1
2
6
'''