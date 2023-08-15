#Hyung Woo Choi - Make a list of prime numbers up to a given number (works with both positive and negative numbers).
#Save the list in a txt file.
#===================================================================================================================

#Prime number list function. Given the prompt to input the range number.
#Returns the list of prime numbers
def primeListMaker():
    #The list of prime numbers.
    primeNumb = []

    #Input the highest number for the 'For' loop range.
    countRange = input("Up to how high the number?")

    #number of task to be done. Will keep the while loop going until all the tasks are done.
    task = 1

    while task > 0 :
        #Boolean to check if number is a negative number or positive.
        isNegative = False

        #If the first character of the string is a '-', remove it and change the above boolean to true.
        if countRange[0] == '-':
            countRange = countRange.strip("-")
            print(countRange)
            isNegative = True

        #If the input is a number do one of the following.
        if countRange.isnumeric() == True:
            
            #put int() to convert the countRange value to number.
            #Check if countRange is greater than 1.
            if int(countRange) > 1:
                #Have '+1' on countRange so that the range number itself is included.
                #Example: if range of 10, the for loop counts from 2 to 10 instead of 2 to 9.
                for i in range(2, int(countRange) + 1):
                    #Boolean to check if it is prime. Starts true thn becomes false if number can be divided by 
                    #another.
                    isPrime = True

                    #Count up from 2 to i.
                    #Divide every number with i to check if there are no remainders after.
                    #If no remainder, the number can be divided by said number and therefore not prime.
                    for x in range(2, i):
                        #If x is not the same as the number i.
                        if x != i:
                            if (i % x) == 0:
                                isPrime = False
                                break

                    #If the number is prime, add it to the primNumb list.
                    if isPrime == True:
                        if isNegative == False:
                            primeNumb.append(i)
                        else:
                            primeNumb.append(-i)
                task -= 1
            #If the countRange is 1, print a message to let user know that 1 or -1 is not a prime.
            elif int(countRange) == 1:
                if isNegative == False:
                    print("Prime must be larger than 1.")
                    task -= 1
                else:
                    print("Prime must be lower than -1")
                    task -= 1
            else:
                #0 cannot be a prime number.
                print("Technically any number multiplied by 0 is 0, so not a prime number")
                task -= 1

        else:
            #If the input is not a number try again.
            print("Not a number, try again.")
            countRange = input("Up to how high the number?")
    return primeNumb

#--------------------------------------------------------------------------------------------------------------

#Puts the inputed list into a text file called 'results.txt'.
#If such file exists, overwrites it.
#If no such file exists, makes one.
def primeTextWrite(primeList):
    #Make the 'results.txt' file. The file will contain the list of all the prime numbers found in a string.
    with open("results.txt", "w") as resultsFile:
        #Smaller list that breaks down the primeNumb list into smaller bits 
        #so that the list won't be a long line in the text file.
        listLimit = 10
        finalListLimit = listLimit
        tempList = []
        for z in range(len(primeList)):
            if z == finalListLimit:
                #When the lineLimit is reach, write the tempList on the current line in the text file
                #then move on a new line. Clear the tempList to repeat the process.
                resultsFile.write(str(tempList)+ "\n")
                tempList.clear()

                #Update the listLimit to do this for the next set of limit.
                finalListLimit += listLimit

            tempList.append(primeList[z])

            #When the end of the primeNumb list is reach, write whatever is left of the tempList
            #onto the new line in the text file.
            if z == len(primeList) - 1:
                resultsFile.write(str(tempList))
                    
                resultsFile.close()

#--------------------------------------------------------------------------------------------------------------

#Reads the 'results.txt' file then prints out the contents.
def primeTextRead(fileDirectory):
    try:
        #Opens the txt file in read only.
        with open(fileDirectory, "r") as readFile:
            print("This is the text file contents")
            print()
            print(readFile.read())
            readFile.close()
    except:
        print("No such file exists")

#--------------------------------------------------------------------------------------------------------------

#Write a text file using the primeListMaker function.
primeTextWrite(primeListMaker())

#Read and print the text file and its contents
primeTextRead("results.txt")