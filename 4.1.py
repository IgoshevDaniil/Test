a = ['']*47
a[0] = 1
a[1] = 1
i=1
print(a[0])
while(i <=45):
    a[i+1] = a[i-1] + a[i]
    print(a[i])
    i += 1
