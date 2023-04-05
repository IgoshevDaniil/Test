import random
a = int(input("Введите число от 0 до 9"))
b = int(input("Ещё раз введите число от 0 до 9"))
arr=[0]*10
i=0
while(i < len(arr)):
    arr[i]=random.randint(0,100)
    i+=1
print(arr)
print(arr[a] + arr[b])