r=int(input())
c=int(input())
l=[]
l1=[]
for i in range(r):
    for j in range(c):
        t=int(input())
        l1.append(t)
    l.append(l1)
    l1=[]
for i in range(r):
    for j in range(c):
        if l[i][i]==0 and l[i][j+1]==0:
            if l[i+1][j]==0 and l[i+1][j=1]==0: