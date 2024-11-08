physics=int(input("enter marks in physics:"))
chemistry=int(input("enter marks in chemistry:"))
maths=int(input("enter marks in maths:"))
biology=int(input("enter marks in biology:"))
computer=int(input("enter marks in computer:"))
total=physics+chemistry+maths+biology+computer
print("total marks=",total)
percentage=(total/500)*100
print("percentage=",percentage)
if percentage>=90:
    print("Grade A")
elif percentage>=80:
    print("Grade B")
elif percentage>=70:
    print("Grade C")
elif percentage>=60:
    print("Grade D")
else:
    print("failed")
