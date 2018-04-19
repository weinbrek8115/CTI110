#Enter 5 test grades and figure out average
#17 April 2018
#CTI-110 P5HW1 - Test Average and Grade
#Karla Weinbrenner


def main():

    #ask user to enter 5 test grades
    #Display letter grades for each test
    
    testScore1 = int(input("Enter value for test score 1: "))
    testScore2 = int(input("Enter value for test score 2: "))
    testScore3 = int(input("Enter value for test score 3: "))
    testScore4 = int(input("Enter value for test score 4: "))
    testScore5 = int(input("Enter value for test score 5: "))
  

    for score in [testScore1,testScore2,testScore3,testScore4,testScore5]:
        
       
        if score >=90:
            print ("Your grade is: A", score)
        elif score >=80:
            print ("Your grade is: B", score)
        elif score >=70:
            print ("Your grade is: C", score)
        elif score >=60:
            print ("Your grade is: D", score)
        else :
            print ("Your grade is: F", score)


            
    calc_average=int(testScore1+testScore2+testScore3+testScore4+testScore5)
    average=calc_average/5


    print("The average of the tests are: ",average)


    


main()
