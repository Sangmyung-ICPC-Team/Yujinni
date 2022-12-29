import sys
input=sys.stdin.readline
s1,s2=map(int,input().split())
if s1*10<5000:
    p1=s1*10
else:
    p1=s1*10-500
result1=s2*10/p1
n1,n2=map(int,input().split())
if n1*10<5000:
    p2=n1*10
else:
    p2=n1*10-500
result2=n2*10/p2
u1,u2=map(int,input().split())
if u1*10<5000:
    p3=u1*10
else:
    p3=u1*10-500
result3=u2*10/p3
find=[result1, result2, result3]
wow=find.index(max(find))
if wow == 0:
    print('S')
elif wow==1:
    print('N')
elif wow==2:
    print('U')