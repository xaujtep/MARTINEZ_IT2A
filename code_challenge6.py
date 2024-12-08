name = input("Enter your name: ")

prelim = eval(input("PRELIM GRADE: "))
midterm =  eval(input("MIDTERM GRADE: "))
sfinals = eval(input("SEMI FINAL GRADE: "))
finals =  eval(input("FINALS GRADE: "))
quiz =  eval(input("QUIZ GRADE: "))
project =  eval(input("PROJECT GRADE: "))

if (prelim >= 65 and prelim <= 100) and (midterm >= 65 and midterm <= 100) and (sfinals >= 65 and sfinals <= 100) and (finals >= 65 and finals <= 100) and (quiz >= 65 and quiz <= 100) and (project >= 65 and project <= 100):
	finalgrade = (prelim * 0.15) + (midterm * 0.15) + (sfinals * 0.15) + (finals* 0.15) + (quiz * 0.25) + (project * 0.15)
	if finalgrade >= 75:
		print("CONGRATULATIONS, YOU PASSED THE COURSE")
	else:
		print("YOU FAILED")
else:
	print("INVALID GRADE")
