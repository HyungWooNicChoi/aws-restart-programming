#numbBanana = input("How many?")

#number of task to be done. Will keep the while loop going until all the tasks are done.
#task = 1

#while task > 0 :
#    if numbBanana.isnumeric() == True:
#        #if the input is a number do one of the following
#        #put int() to convert the numbBanana value to number
#        if int(numbBanana) >= 5 :
#            print("Alot of banans")
#            task -= 1
#        elif int(numbBanana) > 1 and int(numbBanana) < 5 :
#            print("Few bananas")
#            task -= 1
#        elif int(numbBanana) == 1 :
#            print("A banana")
#            task -= 1
#        else:
#            print("No bananas")
#            task -= 1
#    else:
#        #if the input is not a number try again
#        print("Not a number, try again.")
#        numbBanana = input("How old?")

employee_age = [25, 18, 40, 35, 60, 55, 27]

age_threshold = 50

#for e_age in employee_age:
#    if e_age < age_threshold:
#        print(e_age)

#result = [age for age in employee_age if age < 50]
#print(result)

forResult = []

for i in range(len(employee_age)):
    if employee_age[i] < age_threshold:
        forResult.append(employee_age[i])

#print(forResult)
def ascendingOrder(orderList):

    print(orderList)
    print()

    orderedResult = []
    confirmResult = []

    for a in range(len(orderList)):
        orderedResult.append(orderList[a])
    for b in range(len(orderedResult)):
        confirmResult.append(orderList[b])
    #print(orderedResult)

    isSame = False

    while isSame == False:
        for c in range(len(orderedResult)):
            confirmResult[c] = orderedResult[c]

        for x in range(len(orderList)-1):
            if orderedResult[x] > orderedResult[x+1]:
                tempVal = orderedResult[x]
                orderedResult[x] = orderedResult[x+1]
                orderedResult[x+1] = tempVal
                print(orderedResult)

        print("Checker: ")
        print(confirmResult)
        print("========================")

        for y in range(len(orderedResult)):
            if orderedResult[y] == confirmResult[y]:
                isSame = True
            else:
                isSame = False
                break
            
    print("Final result: ")
    print(orderedResult)

    return orderedResult

myResult1 = ascendingOrder(forResult)
print(myResult1)

print()

myResult2 = ascendingOrder(employee_age)
print(myResult2)