
n = int(input())

total = (n*(n+1))/2

number = [int(x) for x in input().split()]
N = sum(number)
print(int(total-N))
