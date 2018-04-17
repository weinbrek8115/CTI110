#CTI 110
#P5T1: Kilometer Convertor
#Karla Weinbrenner
#17 April 2018

CONVERSION_FACTOR = 0.6214

def main ():
    #Get the distance in kilometers
    kilometers = float(input("Enter a distance in kilometers: "))

    #Display the distance converted to miles
    show_miles(kilometers)

def show_miles(km):
    #calculate miles
    miles=km*CONVERSION_FACTOR

    #display the miles
    print(km,"kilometers equals", miles, "miles.")

main()
