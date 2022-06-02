f=open('26-k6.txt','r')
N,K=map(int,f.readline().split())
a=[list(map(int,f.readline().split())) for i in range(N)]
a.sort(key=lambda x: (x[1]/x[0], -x[0]))
b=a[0:K]

print(b)
s,c,m=0,0,0
for x in b:
    s+=x[0]
    if x[0]>m:
        m=x[0]
        c=x[1]
print(s,c)


