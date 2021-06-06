import getpass
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
print("Your username and password is saved.")
username1 = input("Enter your username: ")
password1 = getpass.getpass("Enter your password: ")
if username == username1 and password == password1:
    print("Verified")
while username != username1 or password != password1:
    print("Invalid Username or password")
    username1 = input("Enter your username: ")
    password1 = getpass.getpass("Enter your password: ")
print("Verified.")
