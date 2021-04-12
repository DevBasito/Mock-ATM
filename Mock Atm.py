import random
database = {8944617295: ['Basit', 'Ade', 'baxx@gmail.com', 'password101', 1000]}
"""
Added items to the dictionary because of the logIn Option without having to register first
The register option works fine too
"""

def init():
    isValidOption = False
    print('='*50)
    print('Welcome to Bank FTMB!!!')
    print('='*50)

    haveAccount = int(input('Do you have an Account with us 1-(YES) 2-(NO): \n'))
    if (haveAccount == 1):
        logIn()
    elif (haveAccount == 2):
        register()
    else:
        print('Invalid Option Selected')
        init()


def register():
    print('*********Register*********')
    firstName = input('What is your First Name \n')
    lastName = input('What is your Last Name \n')
    email = input('What is your Email Address \n')
    pword = input('Create a secure Password for yourself \n')
    accountNumber = generatingAcctNum()
    balance = 0

    database[accountNumber] = [firstName, lastName, email, pword, balance]
    print('='*50)
    print(f'Your New Account Number is {accountNumber}')
    print('='*50)
    print('\n')
    
    logIn()


def logIn():
    print('*********Log In*********')

    acctnumFromUser = int(input("Please Enter your Account Number \n"))
    password = input('Enter your Password \n')

    for accountNumber, userDetails in database.items():
        if (acctnumFromUser == accountNumber):
            if (userDetails[3] == password):
                bankOperations(userDetails)
            
            else:
                print('Invalid account or password')
                logIn()


def generatingAcctNum():
    return random.randrange(1111111111, 9999999999)

def bankOperations(user):
    print('='*50)
    print(f'Welcome {user[0]} {user[1]}')
    print('='*50)
    option1 = int(input('What do you want to do (1)-Deposit (2)-Withdrawal (3)-Balance Inquiry (4)-Complaint (5)-Exit (6)-LogOut \n'))

    if (option1 == 1):
        deposit(user)
    elif (option1 == 2):
        withdrawal(user)
    elif (option1 == 3):
        bal_inquiry(user)
    elif (option1 == 4):
        complaint()
    elif (option1 == 5):
        exit()
    elif (option1 == 6):
        logout()
    else:
        print('Invalid Option Selected')
        bankOperations(user)


def deposit(balance):
    deposit = int(input('How much would you like to deposit: \n'))
    balance[4] += deposit
    print(f'You have successfully deposited {deposit}. Your Current Account Balance: NGN {balance[4]}')
    print('Thank you for banking with us')   

def withdrawal(balance):
    withdrawal = int(input('How much would you like to withdraw: \n'))

    if (withdrawal > balance[4]):
        print('Insufficient Funds!!!')
        logIn()
    else:
        balance[4] -= withdrawal
        print(f'You have successfully withdrawn {withdrawal}. Your Current Account Balance: NGN {balance[4]}')
        print('Thank you for banking with us')

def bal_inquiry(balance):
    print(f'Your Current Account Balance: NGN {balance[4]}')
    print('Thank you for banking with us') 

def complaint():
    complaint = input('What issue will you like to report? \n')
    print('Thank you for contacting us. Your Issue will be resolved soon')

def logout():
    logIn()

init()    


