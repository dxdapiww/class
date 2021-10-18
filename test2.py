import turtle,time
n=int(input())
def fact(n):
    x=0
    for i in range(1,n+1):
        m=1
        for j in range(1,i):
            m*=j
            x+=m
    return x        
sum=fact(n)
print(sum)


