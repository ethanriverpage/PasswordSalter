"""
This is the function that Lambda will call using it's lambda_handler. Calling this file runs
'dynamicsalter_lambda.py'
"""

import dynamicsalter_lambda


def lambda_handler(event, context):
    """
    Prints to ensure success, runs main function
    """
    print("Lambda deploy!")
    dynamicsalter_lambda.main()
