my_string = input()
last_char =""
current = 0
maxi = 1

for i in my_string:
    if i == last_char:
        current+=1
        if current>maxi:
            maxi = current
    else:
        current = 1
        last_char = i
print(maxi)