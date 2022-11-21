num=int(input())
l={0,1,2,5,6,8,9}
c=1
n=1
p=1
while c<=num:
    f=0
    prev=n
    while n:
        if n%10 in l:
            n=n//10
        else:
            f=1
            break
    if f==0:
        p=prev
        c+=1
    n=prev+1
print(p)