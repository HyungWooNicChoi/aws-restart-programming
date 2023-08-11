numbBanana = input("How many?")

#number of task to be done. Will keep the while loop going until all the tasks are done.
task = 1

while task > 0 :
    if numbBanana.isnumeric() == True:
        #if the input is a number do one of the following
        #put int() to convert the numbBanana value to number
        if int(numbBanana) >= 5 :
            print("Alot of banans")
            task -= 1
        elif int(numbBanana) > 1 and int(numbBanana) < 5 :
            print("Few bananas")
            task -= 1
        elif int(numbBanana) == 1 :
            print("A banana")
            task -= 1
        else:
            print("No bananas")
            task -= 1
    else:
        #if the input is not a number try again
        print("Not a number, try again.")
        numbBanana = input("How old?")

