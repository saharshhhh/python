import streamlit as st

class Bank:
    def __init__(self):
        # Initialize session state variables
        if "balance" not in st.session_state:
            st.session_state.balance = 0
        if "verified" not in st.session_state:
            st.session_state.verified = False
        if "operation" not in st.session_state:
            st.session_state.operation = None

    def deposit(self):
        dep = st.number_input("Enter the amount to be deposited", min_value=0, max_value=10000, step=1, key="deposit_input")
        if st.button("Deposit"):
            if dep > 10000:
                st.warning("Deposit amount is greater than 10000")
            elif dep < 100:
                st.warning("Deposit amount is less than 100")
            elif dep % 100 != 0:
                st.warning("The amount is not divisible by 100")
            else:
                st.session_state.balance += dep
                st.success(f"Deposit successful! Your balance is now {st.session_state.balance}")

    def withdraw(self):
        wd = st.number_input("Enter the amount to be withdrawn", min_value=0, max_value=st.session_state.balance, step=1, key="withdraw_input")
        if st.button("Withdraw"):
            if wd > st.session_state.balance:
                st.warning(f"Withdraw amount is greater than the balance: {st.session_state.balance}")
            elif wd % 100 != 0:
                st.warning("The amount is not divisible by 100")
            else:
                st.session_state.balance -= wd
                st.success(f"Withdrawal successful! Your balance is now {st.session_state.balance}")

    def verify(self):
        pin = st.number_input("Enter the PIN", min_value=1000, step=1, key="pin_input")
        if st.button("Verify"):
            if pin == 1234:
                st.session_state.verified = True
                st.success("PIN verified successfully!")
            else:
                st.warning("Entered PIN is incorrect")

    def options(self):
        if not st.session_state.verified:
            self.verify()
            return

        st.write("Select an operation:")
        op = st.radio("Choose an option", options=["Deposit", "Withdraw", "Exit"], key="operation_choice")

        if op == "Deposit":
            self.deposit()
        elif op == "Withdraw":
            self.withdraw()
        elif op == "Exit":
            st.write("Thank you for using the bank system!")

# Create the Bank object
obj = Bank()
obj.options()
