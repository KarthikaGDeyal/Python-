set1={"Anu","Akhil","Anjaly","Adish","Amrutha"}
set2={"Amrutha","Rohan","Tinu","Sidharth","Adish"}
print("UNION OPERATION")
print("Using union() method:", set1.union(set2))
print("Using pipe operator:",set1|set2)

print("INTERSECTION OPERATION")
print("Using intersection() method:",set1.intersection(set2))
print("Using & operator:",set1&set2)

print("DIFFERENCE OPERATION")
print("Using difference() method:",set1.difference(set2))
print("Using - operator :",set1-set2)

print("SYMMETRIC DIFFERENCE OPERATION")
print("Using symmetric_difference() method:",set1.symmetric_difference(set2))
print("Using ^ operator:",set1^set2)