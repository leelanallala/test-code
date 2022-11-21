l=list(map(str,input().split(",")))
s1=l[0]
s2=l[1]
t=s2[-1]
c=0
for i in s1:
    if i==t:
        c+=1
print(c)