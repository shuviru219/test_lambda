def lambda_handler(event, context):
    a=100
    b=300
    c=a+b
    print "Invoked by Jenkins :)",c
    return "Invoked by Jenkins :)",c
