class Bank:
    bal = 10000
    counter = 1

    def validate(self):
        tries = 1
        while tries <= 3:
            n = input("Enter pin number:")
            pin = "1234"
            if pin == n:
                obj.view()
            else:
                tries = tries+1
                if tries == 3:
                    print("Too many chances")
                else:
                    print("Please enter a valid pin number")

    def view(self):
        while True:
            print("1.Deposit\n2.Withdraw\n3.Balance Enquiry\n0.Exit")
            c = int(input("Choose our option:"))
            if c == 1:
                obj.deposit_amt()
            elif c == 2:
                obj.withdraw_amt()
            elif c == 3:
                obj.balance_enquiry()
            elif c == 0:
                exit()

    def deposit_amt(self):
        deposit = int(input("Enter amount to deposit"))
        if deposit < 100:
            print("Deposit amount should not be lesser than 100/- ")
        elif deposit > 50000:
            print("Deposit amount should not be greater than 50000/- ")
        elif (deposit % 100) != 0:
            print("Deposit amount should be multiple of 100")
        else:
            self.bal = self.bal + deposit
            print("Deposited successfully")

    def withdraw_amt(self):
        while True:
            if self.counter <= 3:
                withdraw = int(input("Enter amount to withdraw"))
                if withdraw < 100:
                    print("Minimum withdrawal amount should be 100/-")
                elif (withdraw % 100) != 0:
                    print("Withdraw amount should be multiple of 100")
                elif withdraw > self.bal:
                    print("Insufficient funds")
                elif withdraw > (self.bal - 500):
                    print("Minimum account balance should be maintained i.e; 500/-")
                elif withdraw > 20000:
                    print("Maximum amount to be withdrawn is only 20000/-")
                else:
                    self.bal = self.bal - withdraw
                    self.counter = self.counter + 1
                    print("Withdraw successful")
                    obj.view()
            else:
                print("Maximum transactions limit reached")
                obj.view()

    def balance_enquiry(self):
        print("Your account balance is", self.bal, "/-")


obj = Bank()
print("Welcome to ABC bank")
obj.validate()
