def infoGather(fileName, name, age, address, phone):
    userInfo = {
        "Name": name,
        "Age": age,
        "Address": address,
        "Phone": phone
    }

    try:
        for fName in fileName:
            with open(fileName + ".txt", "a+") as f:
                f.write(str(userInfo))

    except Exception as e:
        print("ERROR: Try again later after fixed this problem", e)


fileName = input("Enter your file name > ")
name = input("Enter your name > ")
age = int(input("Enter your age > "))
address = input("Enter your address > ")
phone = int(input("Enter your phone number > "))



"""
try:
    if fileName == int:
        print("Oops! File name must be string not integer.")
    elif name == int:
        print("Oops! Name must be string not integer.")
    # elif age == str or float:
    #     print("Oops! Your age must be a number / integer not string.")
    elif age < 0 or age > 100:
        print("Oops! Invalid age, please input valid age.")
    elif address == int:
        print("Oops! Address must be string not interger.")
    elif phone == str:
        print("Oops! Number must be integer / digit not string.")
    elif phone < 0 or phone > 11:
        print("Oops! Invalid number, please input valid number.")
    else:
        infoGather(fileName, name, age, address, phone)
except Exception as e:
    print("ERROR: There are some problem, please fixed the problem and try agian.", e)
"""



infoGather(fileName, name, age, address, phone)
