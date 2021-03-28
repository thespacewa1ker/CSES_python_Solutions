
n = int(input())
count =0
arr = [int(x) for x in input().split()]


for i in range(1,n):
    if arr[i]<arr[i-1]:
        count+= abs(arr[i]-arr[i-1])
        arr[i]=arr[i]+abs(arr[i]-arr[i-1])
print(count) 
        

