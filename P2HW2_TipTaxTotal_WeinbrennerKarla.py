# CTI-110
# P2HW2 - Tip Tax Total
# Karla Weinbrenner
# 15 Feb 18

#Get food cost
foodCost=float(input ("enter the food cost"))

# Calculate the tip amount at 18 percent of total cost 0.18
tipAmount=foodCost * 0.18


# Calculate the  sales tax at 7 percent of total coat 0.07
salesTax=foodCost * 0.07

total=foodCost+tipAmount+salesTax


# Display the Total cost

print ("The tip is $",format (tipAmount, ",.2f") )
print ("The tax is $",format (salesTax, ",.2f") )
print ("The total is $",format (total, ",.2f") )
