username = input("Enter your username: ")
password = input("Enter your password: ")
print("Your username and password are saved.")

username1 = input("Enter your username: ")
password1 = input("Enter your password: ")
if username == username1 and password == password1:
    print("Verified")
elif username != username1 or password != password1:
    print("Invalid Username or password")
    username1 = input("Enter your username: ")
    password1 = input("Enter your password: ")
