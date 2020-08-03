def revRecur(n, ro=0):
    if n//10==0:
        return (ro*10)+n
    else:
        return revRecur(n//10,(10*ro)+(n%10))


print(revRecur(int(input('Ведите число: '))))