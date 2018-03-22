# CTI-110
# P4HW1 Distance Traveled
# Karla Weinbrenner
# 22 Mar 2018


#Ask the speed of the vehicle
#Ask the number of hours traveled
#Displays the distance the vehicle has traveled for each hour
distance=0

#Get value for speed of vehicle
mph=int(input("What is the speed of vehicle in mph? "))

#Get amount of time traveled
hrs=int(input("How many hours has the vehicle traveled? "))

print ("Hours\t\tDistance Traveled")
print ("--------------------------")

for hours in range (1, hrs+1):
    distance=mph*hours
    print (hours, "\t\t", distance)
    
