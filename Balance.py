class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        if initial_balance<0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_holder=account_holder
        self.__balance=float(initial_balance)
    def deposit(self, amount: float):
        if amount<=0:
            print("Deposit amount must be greater than zero.")
            return
        self.__balance+=amount
        print(f"Deposited ₹{amount:.2f}. New Balance: ₹{self.__balance:.2f}")
    def withdraw(self, amount: float):
        if amount<=0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount>self.__balance:
            print(f"Insufficient funds! Available balance: ₹{self.__balance:.2f}")
            return
        self.__balance-=amount
        print(f"Withdrew ₹{amount:.2f}. Remaining Balance: ₹{self.__balance:.2f}")
    def check_balance(self)->float:
        print(f"Account Holder: {self.account_holder} | Current Balance: ₹{self.__balance:.2f}")
        return self.__balance
account=BankAccount("Rahul Sharma", 5000.0)
account.check_balance()
account.deposit(1500.50)
account.withdraw(2000.0)
account.withdraw(6000.0)
