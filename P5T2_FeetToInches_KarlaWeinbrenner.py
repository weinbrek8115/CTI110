#Feet to Inches
#17 April 2018
#CTI-110 P5T2_FeetToInches
#Karla Weinbrenner


#Constant for the number of inches per foot
INCHES_PER_FOOT = 12

#main function
def main():
    #get a number of feet from the user
    feet = int(input("Enter a number of feet:"))

    #convert that to inches

    print(feet, "feet equals", feet_to_inches(feet), "inches")
    
#the feet_to_inches function converts feet to inches
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT


main()
