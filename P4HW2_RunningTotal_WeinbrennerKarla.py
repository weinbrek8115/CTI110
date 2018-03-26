#CTI-110
#P4HW2
#Karla Weinbrenner
#22 March 2018

#Write a program that asks the user to enter a series of numbers
#It should loop, adding these numbers to a running total
#Until a negative number is entered, the program should exit the loop
#Print the total before exiting

#accumulator variable
runningTotal=0
count=0

userInput=int(input("Enter a number or negative number to exit: "))
print ()

while userInput >=0:
    runningTotal=runningTotal+userInput
    count=count+1

    userInput=int(input("Enter a number or a negative number to exit: "))
    print()

print ("The running total is: ", runningTotal)
