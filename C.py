#C
import sys
sys.setrecursionlimit(int(1e6))
# ans=set()
# for st in range(1,101):
#     for ed in range(st+1,101):
#         ans.add((st+ed)*(ed-st+1)//2)
# for i in range(1,101):
#     if i not in ans:
#         print(i)
n=int(input())
nums=list(map(int,input().split()))
ans=0
for i in nums:
    x=i
    flag=0
    while x>1:
        if x%2:
            flag=1
            break
        x//=2
    if not flag: ans+=1
print(ans)
'''
3
3 6 8
'''
