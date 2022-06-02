def f(n):
    s=''
    while n>0:
        s=str(n%7)+s
        n//=7
    return s

x=7**2103-6*7**1270+3*7**57-98

print(sum(list(map(int,[i for i in f(x)]))))
