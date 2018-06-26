import re
s=input()
a=[]
b=[]
z=[]
g=[]
h=[]
pattern=re.compile('(\d)')
pattern1=re.compile(r'(\D)')
matches=pattern.finditer(s)
matches1=pattern1.finditer(s)
for match in matches:
    a.append(match.group(1))
for match1 in matches1:
    b.append(match1.group(1))
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
