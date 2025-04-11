def credit(balance,transactions,amount):
    balance+=amount
    transactions.append(amount)
    return(balance,transactions)
    
    
def debit(balance,transactions,amount):
    if amount>balance:
        print("insuficient balance")
    else:
        balance-=amount
        transactions.append(-amount)
    return (balance,transactions)
    
    
def showbalance(balance):
     print("current balance :",balance)
     
     
def last5transactions(transactions):
    print("Transaction History",transactions)
    
    
    
    
    
balance=0
transactions=[]

while (True):
    print("1.Credit")
    print("2.Debit")
    print("3.show balance")
    print("4.last 5 transactions")
    print("5.Exit")
    choice=int(input("enter your choice"))
    if choice==1:
        amount=int(input("Enter the amount"))
        balance,amount=credit(balance,transactions,amount)
    elif choice==2:
        amount=int(input("Enter the amount"))
        balance,amount=debit(balance,transactions,amount)
    elif choice==3:
        showbalance(balance)
    elif choice==4:
        last5transactions(transactions)
    
