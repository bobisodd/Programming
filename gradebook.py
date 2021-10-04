last_semester_gradebook = [["geometry", 80], ["ELA 10", 96], ["chemistry", 97], ["AM History", 65]]

# Your code below: 
subjects = ["Government", "Algebra 2", "ELA 11", "Cyber Security"]
grades = [98, 97, 85, 88]
gradebook = [["Government", 98], ["Algebra 2", 97], ["ELA 11", 85], ["Cyber Security", 88]]
gradebook.append(["studyhall", 100])
gradebook.append(["programming", 93])
gradebook[5][1] = 97
gradebook.remove(["ELA 11", 85])
gradebook.append (["ELA 11", "Pass"])
print(gradebook)

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)

