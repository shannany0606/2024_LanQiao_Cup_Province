#E
import sys
from heapq import *
sys.setrecursionlimit(int(1e6))
n,m=map(int,input().split())
s=[]
Q=[]
heapify(Q)
fa=[i for i in range(n)]
ans=0
for i in range(n):
    s.append(input())
def calc(s1,s2):
    s1+=s1
    s2+=s2
    mx=0
    dp=[[0]*(2*m+1) for i in range(2*m+1)]
    for i in range(1,2*m+1):
        for j in range(1,2*m+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=max(dp[i][j],dp[i-1][j-1]+1)
                mx=max(mx,dp[i][j])
    return min(m,mx)

def find(x):
    if x==fa[x]:return x
    fa[x]=find(fa[x])
    return fa[x]

for i in range(n):
    for j in range(i+1,n):
        heappush(Q,(-calc(s[i],s[j]),i,j))
while Q:
    #print(Q)
    x=find(Q[0][1])
    y=find(Q[0][2])
    if x!=y:
        ans-=Q[0][0]
        fa[x]=y
    heappop(Q)
print(ans)
'''
4 4
aabb
abba
acca
abcd
'''