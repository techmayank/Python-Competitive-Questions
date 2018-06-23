m,n=list(map(int,input().split()))
for i in range(0,m):
    c.append(list(map(int,input().split())))
k=int(input())
d=sorted(c,key=lambda x:x[k])
for i in d:
    print(*i)
