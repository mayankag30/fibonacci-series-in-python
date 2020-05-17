n = int(input("Enter the number of fibonacci series elements you want: "))
a = 0
b = 1
print(a,",",b,",",end=" ")
for i in range(0,n-2):
    c = a+b
    print(c,",",end=" ")
    a=b
    b=c


