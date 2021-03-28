
n = int(input())

if n>=4:
    for i in range(2,n+1,2):
        print(i)
    for i in range(1,n+1,2):
        print(i)
elif n==1:
    print(n)
else:
    print("NO SOLUTION")