#take input
row = int(input("please enter the total number of rows  : "))
number = 1 #initialise by 1

print(" floyds traingle")
#outer  loop for number of rows
for i in range(1, row + 1):
    #inner loop for number of columns
    for j in range(1, i + 1):
        #display result
        print(number, end = '   ')
        number = number + 1
    print()