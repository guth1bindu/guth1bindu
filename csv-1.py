import csv
with open('customer.csv','w',newline='')as f:
    w=csv.writer(f)
    w.writerow(['bank_name','customer_no','account_no','credited_amount','debited_amount','current_balance'])
    n=int(input("enter no of banks"))
    for i in range(n):
        bankn_ame=input("enter bank name")
        customer=input("enter customer name")
        account_no=int(input("enter account no"))
        credited_amount=float(input("enter credited mount "))
        debited_amount=float(input("enter debited amount"))
        bal=credited_amount-debited_amount
        current_balance=float(input("current balance"))
        w.writerow(['bank_name','customer_no','account_no','credited_amount','debited_amount','current_balance'])
    print("total customers data written completely")