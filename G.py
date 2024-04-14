#G
import sys
sys.setrecursionlimit(int(1e6))
n,m,T=map(int,input().split())
R=list(map(int,input().split()))
C=list(map(int,input().split()))

mp={}
cnt=0
a=R.copy()
a.sort()
for x in a:
    if x not in mp:
        cnt+=1
        mp[x]=cnt
for i in range(n):R[i]=mp[R[i]]

mp.clear()
cnt=0
a=C.copy()
a.sort()
for x in a:
    if x not in mp:
        cnt+=1
        mp[x]=cnt
for i in range(n):C[i]=mp[C[i]]

#print(R)
#print(C)

mod=int(1e9+7)
jc=[1]
for i in range(1,int(2e5)+1):
    jc.append(jc[-1]*i%mod)

def ksm(T,n):
    S=1
    while n:
        if n%2:S=S*T%mod
        T=T*T%mod
        n//=2
    return S

def calc(x,y):
    return jc[x]*ksm(jc[y],mod-2)%mod*ksm(jc[x-y],mod-2)%mod

for _ in range(T):
    str,stc,edr,edc=map(int,input().split())
    str=R[str-1]
    stc=C[stc-1]
    edr=R[edr-1]
    edc=C[edc-1]
    if edr-str<=0 or edc-stc<=0:print(0)
    else: print(calc(edr-str+edc-stc,edr-str))

'''
4 4 2
4 2 3 1
2 1 2 1
4 4 1 1
2 2 2 4
'''