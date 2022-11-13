import hashlib
import requests

username = input("Enter username: ")
password = input("Enter password: ")
creationdate = input("Enter account creation date: ")
api_url = "https://yesno.wtf/api"

global staticsalt
staticsalt = ""

def restapi_request():
        print("Contacting the REST API...")
        try:
            response = requests.get(api_url)
            json_data = response.json() if response.status_code == 200 else None
            if json_data and 'answer' in json_data:
                api_answer = json_data['answer']
                print("API answered: " + str(api_answer))
                global staticsalt
                staticsalt = str(api_answer)
        except requests.exceptions.RequestException as e:
            print("Request to REST API failed. Check your internet connection and try again later.")
        pass

def staticsalting():
    global staticsalt
    while True:
        restapiinput = input("Would you like to pull a random salt, or use your own? Type 'random' for random or 'input' for choosing your own: ")
        if restapiinput not in ["random","input"]:
            print(str(restapiinput) + " is not a valid option. Valid choices are 'random' or input'.")
            continue
        else:
            break
    if restapiinput == str("random"):
        print("Using random answer from " + api_url + " REST API")
        restapi_request()
    elif restapiinput == str("input"):
        staticsalt = input("Input your static salt: ")

    staticsaltfullstring = str(f"{password}{staticsalt}")
    staticsalthashobject = hashlib.sha512(staticsaltfullstring.encode())
    print("Statically salted SHA512 hash: " + staticsalthashobject.hexdigest() + " using salt: " + str(staticsaltfullstring))
    


def dynamicsalting():
    inputMerged = str(f"{username}{password}{creationdate}")
    fullstring = str(inputMerged) + str(len(inputMerged))
    hash_object = hashlib.sha512(fullstring.encode())
    print("Dynamically salted sha512 hash: " + hash_object.hexdigest() + " using salt: " + fullstring)

def nosalting():
    nosalthashobject = hashlib.sha512(password.encode())
    print("Unsalted sha512 hash: " + nosalthashobject.hexdigest())

def salting():
    while True:
        salttypeinput = input("Would you like your credentials statically or dynamically salted? ")
        if salttypeinput not in ["static","dynamic"]:
            print(str(salttypeinput) + " is not a valid option. Valid choices are 'static' or 'dynamic'. Please choose a valid salt type.")
            continue
        else:
            break
    if salttypeinput == str("static"):
        staticsalting()
    elif salttypeinput == str("dynamic"):
        dynamicsalting()

def handler():
    while True:
        saltedquestion = input("Would you like your password salted? Type Y for yes and N for no. ")
        if saltedquestion not in ["Y","N"]:
            print("Please type Y or N to continue.")
            continue
        elif saltedquestion == "Y":
            salting()
            exit()
        else:
            nosalting()
            exit()
    


    


