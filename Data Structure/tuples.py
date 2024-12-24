# tuples = collection which is ordered and unchangeable
#          used to group together related data

students = ("Prashast",36,"male")

print(students.count("Prashast"))
print(students.index("Prashast"))

for x in students:
    print(x)

if "Prashast" in students:
    print("Prashast is here!!!!!")