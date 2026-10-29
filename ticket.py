age = int(input("Enter your age: "))
is_student = str(input("Are you a student?(Yes/No): "))

if age < 7:
    print("Tickets ar free.")

elif age > 65:
    print("Tickets ara 4 manats.")

elif is_student == 'Yes':
    print("Tickets are 5 manats.")

else:
    print("Tickets ara 8 manats.")