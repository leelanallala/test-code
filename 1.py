n=int(input())
if n == 0:
    print(0)
s=""
while n:
    s=s+str(int(n%3))
    n //=3
print(s)