user_email = 'slimovalalaa@gmail.com'
user_password = '12345678'

email = str(input("Eneter your email: "))
password = str(input("Enter your password: "))

if email == user_email and password == user_password:
    print("Welcome!")

elif email != user_email:
    print("Email not found")

elif password != user_password:
    print("Password is wrong")

