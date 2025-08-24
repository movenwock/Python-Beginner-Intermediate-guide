# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Brian",19,"male")

print(student.count("Brian"))
print(student.index("male"))

for x in student:
    print(x)

if "Brian" in student:
    print("Brian is here!")