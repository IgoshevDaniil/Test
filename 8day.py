a = ['']*1
n = int(input())
while(n>0):
    if ((n%2)==0):
        a.append('0')
    else:
        a.append('1')
    n=n//2
i = 1
while(i<=len(a)):
    print(a[-i], end=(''))
    i += 1
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
