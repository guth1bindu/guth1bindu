import logging
logging.basicConfig(filename="bindu1.txt",level=logging.INFO)
logging.info("a new request came")
try:
    a=int(input("enter a number"))
    b=int(input("enter b number"))
    c=a/b
    print(c)
except ZeroDivisionError as msg:
    print("can not divide with zero")
    logging.exception(msg)
except ValueError as msg:
    print("only interger values accepted")
    logging.exception(msg)
logging.info("request is completed")