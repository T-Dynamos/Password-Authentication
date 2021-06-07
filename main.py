
import getpass
h1 = '================================'
def register():
    username = input("Please input your desired username =  ")
    password = getpass.getpass("Please input your desired password =  ")
    file = open("accountfile.txt","a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    print(" Registration Successful !")
def login():
    username = input("Please enter your username = ")
    password = getpass.getpass("Please enter your password = ")  
    for line in open("accountfile.txt","r").readlines():
        login_info = line.split() 
        if username == login_info[0] and password == login_info[1]:
            print("Correct credentials!")
            return True
            exit()
    print("Incorrect credentials.")
    exit()
    print("Try Again")
    return login()
print(h1)
print("Do you want to Login or Register")
print(h1)
a = input("[(login (l) /register (r)] ==> ")
if a == 'login':
	login()
if a == 'register':
	register()
if a == 'l':
	login()
if a == 'r':
	register()
else:
	exit()
