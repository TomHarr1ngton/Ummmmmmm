
def prime(n):
    for Del in range(2,int(n**0.5)+1):
        if n%Del==0 :
            return False
    return True
k=0
for i in range(500000,1,-1):
    d=set()
    for Del in range(2,int(i**0.5)):
        if i%Del==0:
            if prime(Del)==True:
                d.add(Del)
            if prime(i//Del)==True:
                d.add(i//Del)
    if sum(d)!=0 and sum(d)%10==0:
        k+=1
        print(i,sum(d))
        if k==7:
            break
