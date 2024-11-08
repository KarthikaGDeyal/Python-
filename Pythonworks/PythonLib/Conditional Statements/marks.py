physics=float(input("enter the marks of physics:"))
chemistry=float(input("enter the marks of chemistry:"))
biology=float(input("enter the marks of biology:"))
maths=float(input("enter the marks of maths:"))
computer=float(input("enter the marks of computer:"))
total=physics+chemistry+biology+maths+computer
print("total marks out of 500",total)
percentage=(total/500)*100
print("percentage",percentage)
if percentage>=90:
    print("A Grade")
elif percentage>=80:
    print("B Grade")
elif percentage>=70:
    print("C Grade")
elif percentage>=60:
    print("D Grade")
elif percentage>=50:
    print("E Grade")
else:
    print("Failed!!..")
