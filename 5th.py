# num = int(input("Enter a number:"))
total = 0
for i in range(1,11):
    total+=i
print("SUM =", total)



for i in range(1,51):
    if i % 2 == 0:
        print(i,end="|")