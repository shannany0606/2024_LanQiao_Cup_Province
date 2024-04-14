#H
import sys
sys.setrecursionlimit(int(1e6))
n=int(input())
X=list(map(int,input().split()))
tnxt=[[0,0] for i in range(int(1e5+10))]
End=[[0,0]]*int(1e5+10)
cnt=0
for i in range(n):
    x=X[i]
    u=0
    for d in range(30,-1,-1):
        if x&(2**d):sta=1
        else:sta=0
        if not tnxt[u][sta]:
            cnt+=1
            tnxt[u][sta]=cnt
        u=tnxt[u][sta]
    End[u]=[1,i]

E=[[] for i in range(int(1e5+10))]
f=list(map(int,input().split()))
for i in range(n):
    if f[i]==-1:continue
    E[f[i]].append(i)
    E[i].append(f[i])

def dfs(u,x,d,ban):
    if d<0:
        if End[u][0] and End[u][1] not in ban:
            return X[End[u][1]]
        return -1
    if x&(2**d):sta=1
    else:sta=0
    if tnxt[u][sta^1]:
        tmp=dfs(tnxt[u][sta^1],x,d-1,ban)
        if tmp!=-1:return tmp
    if tnxt[u][sta]:
        tmp=dfs(tnxt[u][sta],x,d-1,ban)
        if tmp!=-1:return tmp
    return -1

ans=0
for i in range(n):
    tmp=dfs(0,X[i],30,E[i])
    if tmp!=-1:ans=max(ans,X[i]^tmp)
print(ans)
'''
5
1 0 5 3 4
-1 0 1 0 1
'''