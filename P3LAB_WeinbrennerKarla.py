# P3LAB_Weinbrenner
# Karla Weinbrenner
# 2 March 2018

# This program takes a number grade and outputs a letter grade.

# system uses 10-point grading scale

# TO DO: define the rest of the scores

grade=int(input("Enter value for grade: "))

def main():
    if grade >=90:
        print ("Your grade is: A")  
    elif grade >=80:
         print ("Your grade is: B")
    elif grade >=70:
        print ("Your grade is: C")
    elif grade >=60:
        print ("Your grade is: D")
    elif grade >=50:
        print ("Your grade is: F")
    



main()
