#D
import sys
sys.setrecursionlimit(int(1e6))
n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(0,n):
    if i>=n-1-i:break
    nxt=n-1-i
    if a[i]==a[nxt]:continue
    if a[i]>a[nxt] and i+1<n-2-i and a[i+1]>a[n-2-i]:
        mn=min(a[i]-a[nxt],a[i+1]-a[n-2-i])
        a[i]-=mn
        a[i+1]-=mn
        ans+=mn
    if a[i]<a[nxt] and i+1<n-2-i and a[i+1]<a[n-2-i]:
        mn=min(a[nxt]-a[i],a[n-2-i]-a[i+1])
        a[i]+=mn
        a[i+1]+=mn
        ans+=mn
    ans+=abs(a[i]-a[nxt])
print(ans)
'''
4
1 2 3 4
'''