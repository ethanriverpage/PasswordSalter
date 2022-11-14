import dynamicsalter_lambda


def lambda_handler(event, context):
    print("Lambda deploy!")
    dynamicsalter_lambda.main()
