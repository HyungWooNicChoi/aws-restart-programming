#Score grading function. Use the 'score' argument to grade them
#Print the grade
#F = fail (Less than 50)
#E = pass (between 50 to 59)
#D = between 60 to 69
#C = between 70 to 79
#B = between 80 89
#A = 90 and above
def markGrading(score):
    if score >= 50 and score < 60:
        print("E")
    elif score >= 60 and score < 70:
        print("D")
    elif score >= 70 and score < 80:
        print("C")
    elif score >= 80 and score < 90:
        print("B")
    elif score >= 90:
        print("A")
    else:
        print ("F")

number = 81

markGrading(number)