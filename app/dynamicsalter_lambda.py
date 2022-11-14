"""
This docstring is because Pylint is annoying
"""
import hashlib
import sys

import requests

global STATIC_SALT
global ERROR_COUNT
STATIC_SALT = ""
ERROR_COUNT = 0


def main():
    """
    Here's a docstring Pylint!
    """
    username = "username"
    password = "password"
    creationdate = "01/01/1970"
    api_url = "https://yesno.wtf/api"

    global STATIC_SALT
    STATIC_SALT = ""

    def restapi_request():
        print("Contacting the REST API...")
        try:
            response = requests.get(api_url, timeout=10)
            json_data = response.json() if response.status_code == 200 else None
            if json_data and "answer" in json_data:
                api_answer = json_data["answer"]
                print("API answered: " + str(api_answer))
                global STATIC_SALT
                STATIC_SALT = str(api_answer)
        except requests.exceptions.RequestException:
            print(
                "Request to REST API failed. Check your internet connection and try again later."
            )

    def staticsalting():
        global STATIC_SALT
        while True:
            restapiinput = "random"
            if restapiinput not in ["random", "input"]:
                print(
                    str(restapiinput)
                    + " is not a valid option. Valid choices are 'random' or input'."
                )
                continue
            else:
                break
        if restapiinput == str("random"):
            print("Using random answer from " + api_url + " REST API")
            restapi_request()
        elif restapiinput == str("input"):
            STATIC_SALT = "reallybadsalt"

        staticsaltfullstring = str(f"{password}{STATIC_SALT}")
        staticsalthashobject = hashlib.sha512(staticsaltfullstring.encode())
        print(
            "Statically salted SHA512 hash: "
            + staticsalthashobject.hexdigest()
            + " using salt: "
            + str(staticsaltfullstring)
        )

    def dynamicsalting():
        input_merged = str(f"{username}{password}{creationdate}")
        fullstring = str(input_merged) + str(len(input_merged))
        hash_object = hashlib.sha512(fullstring.encode())
        print(
            "Dynamically salted sha512 hash: "
            + hash_object.hexdigest()
            + " using salt: "
            + fullstring
        )

    def nosalting():
        nosalthashobject = hashlib.sha512(password.encode())
        print("Unsalted sha512 hash: " + nosalthashobject.hexdigest())

    def salting():
        while True:
            salttypeinput = "static"
            if salttypeinput not in ["static", "dynamic"]:
                print(
                    str(salttypeinput)
                    + " is not a valid option. Valid choices are 'static' or 'dynamic' "
                    + ". Please choose a valid salt type."
                )
                continue
            else:
                break
        if salttypeinput == str("static"):
            staticsalting()
        elif salttypeinput == str("dynamic"):
            dynamicsalting()

    while True:
        saltedquestion = "Y"
        if saltedquestion not in ["Y", "N"]:
            print("Please type Y or N to continue.")
            continue
        elif saltedquestion == "Y":
            salting()
            return 0
        else:
            nosalting()
            return 0


if __name__ == "__main__":
    main()
