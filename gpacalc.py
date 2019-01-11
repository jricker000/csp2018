print "Grades are to be entered in a number scale; 0.0-4.0"


#input grades
grade1 = input("Enter grade of your first class: ")

grade2 = input("Enter grade of your second class: ")

grade3 = input("Enter grade of your third class: ")

grade4 = input ("Enter grade of your fourth class: ")

grade5 = input ("Enter grade of your fifth class: ")

grade6 = input ("Enter grade of your sixth class: ")

grade7 = input ("Enter grade of your seventh class: ")

grade8 = input ("Enter grade of your eigth class: ")

#convert inputs to numbers and potential decimals
grade1 = float(grade1)
grade2 = float(grade2)
grade3= float(grade3)
grade4 = float(grade4)
grade5 = float(grade5)
grade6= float(grade6)
grade7 = float(grade7)
grade8 = float(grade8)

#calculate final
totalGrades = grade1+grade2+grade3+grade4+grade5+grade6+grade7+grade8
gpa = totalGrades/8

print "Your gpa is a: ", + float(gpa)