marks=int(input("Enter your marks:"))
if marks>100 or marks<0:
    print("Invalid Marks")
elif marks>=90:
    print("A+ Grade")
elif marks>=80:
    print("A Grade")
elif marks>=   70:
    print("B+ Grade")
elif marks>=60:
    print("B Grade")
elif marks>=50:
    print("C+ Grade")
elif marks>=35:
    print("C Grade")
else:
    print("Failed")