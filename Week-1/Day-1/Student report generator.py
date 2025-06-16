grade=None
name=None
age=0
english_marks=0
urdu_marks=0
math_marks=0
option='n'
average_marks=0



def avg(english_marks,math_marks,urdu_marks):
    return((english_marks + urdu_marks + math_marks)/3)


name=input("Enter your name : ")
age=int(input("Enter your age : "))
english_marks=float(input("Enter your English marks : "))
math_marks=float(input("Enter your Math marks : "))
urdu_marks=float(input("Enter your Urdu marks : "))

subject_marks = {
"eng":english_marks,
"urdu":urdu_marks,
"math":math_marks,
}

option= input("Do you want to add bonus marks to all subjects? [Y/n]")
if(option=='Y' or option=='y'):
    english_marks += 5
    math_marks += 5
    urdu_marks += 5
    print("Bonus marks added")
else:
    print("No bonus marks added")


average_marks=avg(english_marks,math_marks,urdu_marks)

print(f"Your average marks are : {average_marks}")

if(average_marks>=80):
    print("Your grade is A")
    grade='A'
elif(average_marks>=60 and average_marks<=79):
    print("Your grade is B")
    grade='B'
elif(average_marks>=40 and average_marks<=59):
    print("Your grade is C")
    grade='C'
else:
    print("Your grade is F")
    grade='F'


with open("Report.txt","w") as f:
    f.write(f"Name : {name}\n")
    f.write(f"Age : {age}\n")
    f.write(f"English marks : {english_marks}\n")
    f.write(f"Urdu marks : {urdu_marks}\n")
    f.write(f"Math marks : {math_marks}\n")
    f.write(f"Average :{average_marks}\n")
    f.write(f"Grade : {grade}\n")
    f.close()