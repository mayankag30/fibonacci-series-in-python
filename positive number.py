n = int(input("Enter the number of elements: "))
myList = []
print("Enter numbers: ")
for i in range(0,n):
    number = int(input())
    myList.append(number)
for i in myList:
    if i>0:
        print(i,",",end=" ")
        
    