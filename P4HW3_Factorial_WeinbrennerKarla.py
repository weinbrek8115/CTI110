#CTI 110
#P4HW3 - Factorial
#Karla Weinbrenner
#26March2018

#Ask the user fot a nonnegative integer and use a loop to calculate the factorial
#Display the factorial

number=int(input ("Enter a non-negative integer: "))

product=1
for i in range (number):
    product=product*(i+1)

print ("The factorial of ",number)
print ("is",product)
