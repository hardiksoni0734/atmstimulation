pin = 1234
limit = 20000
singlimit = 10000
minbal = 1000

balance = 25000
daily = 0

wrong = 0
lock = False

transactions = []

def pin_check(pin):
    return pin == pin


def verify():

    global wrong
    global lock

    if lock:
        print("\nAccount is already locked.")
        return False

    while wrong < 3:

        pin = int(input("\nEnter your PIN: "))

        if pin_check(pin):

            print("\nPIN verified successfully.")
            wrong = 0

            return True

        else:

            wrong += 1

            print("Incorrect PIN.")
            print("Attempts remaining:",3 - wrong)

    lock = True

    print("\n⚠ SECURITY ALERT")
    print("Account locked due to 3 incorrect PIN attempts.")

    return False

def cbalance():

    print("\n========== BALANCE ==========")
    print("Available Balance : ₹", balance)
    print("=============================")

def amtcheck(amount):

    if amount <= 0:
        return False, "Amount must be greater than zero."

    if amount % 100 != 0:
        return False, "Amount must be a multiple of ₹100."

    if amount > singlimit:
        return False, "Single transaction limit is ₹10,000."

    return True, "Valid amount."

def chlim(amount):

    if daily + amount > limit:

        remaining = limit - daily

        return False, remaining

    return True, limit - daily - amount

def secchack(amount):

    if amount >= 5000:

        print("\nSecurity verification required.")

        otp = int(input("Enter OTP: "))

        if otp != 5678:

            print("Incorrect OTP.")
            return False

        print("OTP verified.")

    return True

def withdraww():

    global balance
    global daily

    print("\n========== CASH WITHDRAWAL ==========")

    amount = int(input("Enter amount: ₹"))

    valid, message = amtcheck(amount)

    if not valid:

        print("❌", message)
        return

    allowed, remaining = chlim(amount)

    if not allowed:

        print("❌ Daily withdrawal limit exceeded.")
        print("Remaining limit: ₹", remaining)
        return

    if amount > balance:

        print("❌ Insufficient balance.")
        return

    if balance - amount < minbal:

        print("❌ Minimum balance of ₹1,000 must be maintained.")
        return

    if not secchack(amount):

        print("❌ Transaction cancelled for security reasons.")
        return

    oldbal = balance

    balance -= amount
    daily += amount

    transactions.append("Withdrawal : ₹" + str(amount))

    receiptgenarate("WITHDRAWAL",amount,balance)


def deposit():

    global balance

    print("\n========== CASH DEPOSIT ==========")

    amount = int(input("Enter deposit amount: ₹"))

    if amount <= 0:

        print("❌ Invalid deposit amount.")
        return

    oldbal = balance

    balance += amount

    transactions.append("Deposit : ₹" + str(amount))

    receiptgenarate("DEPOSIT",amount,oldbal,balance)

def pinchange():

    global pin

    print("\n========== CHANGE PIN ==========")

    oldpin = int(input("Enter current PIN: "))

    if oldpin != pin:

        print("❌ Incorrect current PIN.")
        return

    newpin = int(input("Enter new PIN: "))
    confirmpin = int(input("Confirm new PIN: "))

    if newpin != confirmpin:

        print("❌ PIN confirmation does not match.")
        return

    if newpin == pin:

        print("❌ New PIN cannot be same as old PIN.")
        return

    if newpin < 1000 or newpin > 9999:

        print("❌ PIN must contain exactly 4 digits.")
        return

    pin = newpin

    print("✅ PIN changed successfully.")


def ministate():

    print("\n========== MINI STATEMENT ==========")

    if len(transactions) == 0:

        print("No transactions available.")

    else:

        for i in range(len(transactions)):

            print(i + 1, ".", transactions[i])

    print("====================================")



def lasttrans():

    print("\n========== LAST TRANSACTION ==========")

    if len(transactions) == 0:

        print("No transaction found.")

    else:

        print(transactions[-1])

    print("======================================")


def sec_stat():

    print("\n========== SECURITY STATUS ==========")

    if lock:

        print("Account Status : LOCKED")

    else:

        print("Account Status : ACTIVE")

    print("Daily Limit    : ₹", limit)
    print("Used Today     : ₹", daily)
    print("Remaining      : ₹", limit - daily)

    print("====================================")



def receiptgenarate(transtype,amount,oldbal,newbalance):

    print("\n====================================")
    print("          ATM RECEIPT")
    print("====================================")

    print("Transaction :", transtype)
    print("Amount      : ₹", amount)
    print("Old Balance : ₹", oldbal)
    print("New Balance : ₹", newbalance)
    print("Status      : SUCCESS")

    print("====================================")


def atm_menu():

    while True:

        print("\n")
        print("================================")
        print("        SMART SECURE ATM")
        print("================================")

        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. Mini Statement")
        print("6. Last Transaction")
        print("7. Security Status")
        print("8. Logout")

        print("================================")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            cbalance()

        elif choice == 2:

            withdraww()

        elif choice == 3:

            deposit()

        elif choice == 4:

            pinchange()

        elif choice == 5:

            ministate()

        elif choice == 6:

            lasttrans()

        elif choice == 7:

            sec_stat()

        elif choice == 8:

            print("\nLogging out securely...")
            print("Thank you for using our ATM.")
            break

        else:

            print("❌ Invalid choice.")


def main():

    print("\n================================")
    print("     WELCOME TO SECURE ATM")
    print("================================")

    authenticated = verify()

    if authenticated:

        atm_menu()

    else:

        print("\nAccess denied.")



main()