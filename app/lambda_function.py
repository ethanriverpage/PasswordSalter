import dynamicsalter_master

def lambda_handler(event, context):
    print("Lambda deploy!")
    dynamicsalter_master.main()

