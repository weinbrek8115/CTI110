#P4T2 Bugs
#Karla Weinbrenner
#22 March 2018

#running total of bugs collected everyday for seven days
#Input number of bugs collected each day
#Display total amount of bugs collected

total=0

for day in range (1,8):
    print ("Enter the number of bugs collected on day ", day)
    bugs=int(input())
    total += bugs

print ("In seven days you collected a total of ", total, "bugs.")
