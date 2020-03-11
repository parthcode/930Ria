'''
Variables
1.int
2.str
3.float
'''
a = int(input("Enter a first number"))
b = int(input("Enter the second number"))

print("Sum is :", a * b)


###############################################################
def signUp(file_path):
    name = input("Enter your name")
    user_name = input("Enter the user name")
    password = input("Etner the password")
    meta_data = open(file_path, 'a')
    data = name + '#' + user_name + '#' + password
    meta_data.write(data)
    meta_data.write('\n')
    meta_data.close()


def logIn(file_path):
    pass


operation = input("Enter 1 to singup 2 to login")
file_path = 'C:/Users/Parth/PycharmProjects/djanjo_all/user_details.txt'
if operation == "1":
    signUp(file_path)
elif operation == "2":
    logIn(file_path)

else:
    print("Enter a valid operation")
###########################################################################

########################################################################
for i in range(5):
    for j in range(i):
        print("*", end='')
    print('\n')
##############################################################
