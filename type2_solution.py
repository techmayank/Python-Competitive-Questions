s=input()
a=[]
b=[]
z=[]
g=[]
h=[]

for i in s:
    if ord(i)<65:
        a.append(i)
    else:
        b.append(i)
c=list(map(int,a))


d=sorted(c,key=lambda x:x%2==0)
for i in d:
    if i%2==0:
        g.append(i)
    else:
        h.append(i)

g=sorted(g)
h=sorted(h)
g=h+g


e=sorted(b,key=lambda x:ord(x)<90)

for i in e:
    if ord(i)>64 and ord(i)<97:
        z.append(i)


for i in z:
    e.remove(i)
z=sorted(z)
e=sorted(e)

e=e+z+g

for i in e:
    print(i,end='')
