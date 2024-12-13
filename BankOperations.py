import streamlit as st
class Bank:
    Balance=0
    def deposit(self):
        dep=st.number_input("Enter the amount to be deposited", min_value=0, max_value=10000, step=1)
        if st.button("Deposit"):
            if dep > 10000:
                st.warning("deposit amount is greater than 10000")
            if dep < 100:
                st.warning("deposit amount is lesser than 100")
            if(dep%100)!=0:
                st.warning("the amount is not divisible by 100")
            else:
                self.Balance += dep
                st.success(f"Deposit successful! Your balance is now {self.Balance}")
    # def withdraw(self):
    #     wd= st.number_input("Enter the amount to be withdrawn", min_value=0.00, max_value=10000, step=0.01)
    def withdraw(self):
        wd=st.number_input("Enter the amount to be withdrawn", min_value=0, max_value=self.Balance, step=1)
        if st.button("Withdraw"):
            if wd > self.Balance:
                st.warning(f"withdraw amount is greater than the balance: {self.Balance}")
            if (wd % 100) != 0:
                st.warning("the amount is not divisible by 100")
            else:
                self.Balance -= wd
                st.success(f"Deposit successful! Your balance is now {self.Balance}")
    def verify(self):
        pin=st.number_input("Enter the pin",min_value=1000)
        if st.button("verify"):
            if pin == 1234:
                self.options()
            else:
                st.warning("Entered pin is incorrect")
                # st.rerun

    def options(self):
        op=st.number_input("Enter your option choice", min_value=0, max_value=3, step=1)
        if st.button("check operation"):
            # match op:
            #     case 1: st.success("asd")
            #             self.deposit()
            #     case 2: self.withdraw()
            if op==1:
                dep = st.number_input("Enter the amount to be deposited", min_value=0, max_value=10000, step=1)
            if op==2:
                obj.withdraw()
obj=Bank()
obj.verify()
