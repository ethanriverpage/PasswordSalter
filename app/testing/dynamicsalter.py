"""
Unused. For testing only.
"""


import hashlib

username = input("Enter username: ")
password = input("Enter password: ")
creationdate = input("Enter account creation date: ")


def staticsalting():
    staticsalt = input("Enter a salt string: ")
    staticsaltfullstring = str(f"{password}{staticsalt}")
    staticsalthashobject = hashlib.md5(staticsaltfullstring.encode())
    print("Statically salted MD5 hash: " + staticsalthashobject.hexdigest())


def dynamicsalting():
    inputMerged = str(f"{username}{password}{creationdate}")
    fullstring = str(inputMerged) + str(len(inputMerged))
    hash_object = hashlib.md5(fullstring.encode())
    print("Dynamically salted MD5 hash: " + hash_object.hexdigest())


def nosalting():
    nosalthashobject = hashlib.md5(password.encode())
    print("Unsalted MD5 hash: " + nosalthashobject.hexdigest())


def salting():
    while True:
        salttypeinput = input(
            "Would you like your credentials statically or dynamically salted? "
        )
        if salttypeinput not in ["static", "dynamic"]:
            print(
                str(salttypeinput)
                + " is not a valid option. Valid choices are 'static' or 'dynamic'. Please choose a valid salt type."
            )
            continue
        else:
            break
    if salttypeinput == str("static"):
        staticsalting()
    elif salttypeinput == str("dynamic"):
        dynamicsalting()


while True:
    saltedquestion = input(
        "Would you like your password salted? Type Y for yes and N for no. "
    )
    if saltedquestion not in ["Y", "N"]:
        print("Please type Y or N to continue.")
        continue
    elif saltedquestion == "Y":
        salting()
        exit()
    else:
        nosalting()
        exit()
