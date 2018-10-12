def lambda_handler(event, context):
    a=1
    b=3
    c=a+b
    print "Invoked by Jenkins",c
    return "Invoked by Jenkins",c
