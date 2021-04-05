t = int(input())
num =1
while t!=0:
    y,x = [int(x) for x in input().split()]
    t =t-1
    if x>y:
        if x%2==1:
            print(x*x-y+1)
        else:
            x=x-1
            print(x*x+y)
    else:
        if y%2 ==0:
            print(y*y-x+1)
        else:
            y= y-1
            print(y*y+x)
    




