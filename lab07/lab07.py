"""Q2 Retirement"""
class Account:
    """An account has a balance and a holder."""
    max_withdrawal = 10
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        if amount > self.max_withdrawal:
            return "Can't withdraw that amount"
        self.balance = self.balance - amount
        return self.balance

    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        year, balance = 0, self.balance
        while balance < amount:
            balance += balance * self.interest
            year += 1
        return year


# a = Account('John')
# print(a.deposit(10))
#     # 10
# print(a.balance)
#     # 10
# print(a.interest)
#     # 0.02
# print(a.time_to_retire(10.25)) # 10 -> 10.2 -> 10.404
#     # 2
# print(a.balance)               # balance should not change
#     # 10
# print(a.time_to_retire(11))    # 10 -> 10.2 -> ... -> 11.040808032
#     # 5
# print(a.time_to_retire(100))
#     # 117


"""Q3: FreeChecking"""
class FreeChecking(Account):
    """
    A bank account that charges for withdrawals, but the first two are free!
    """
    withdraw_fee = 1
    free_withdrawals = 2
    
    def withdraw(self, amount):
        if self.free_withdrawals:
            self.free_withdrawals -= 1
            return Account.withdraw(self, amount)
        else:
            return Account.withdraw(self, amount + self.withdraw_fee)
        

# ch = FreeChecking('Jack')
# ch.balance = 20
# print(ch.withdraw(100))  # First one's free
#     # 'Insufficient funds'
# print(ch.withdraw(3))   # And the second
# #     17
# print(ch.balance)
# #     17
# print(ch.withdraw(3))    # Ok, two free withdrawals is enough
# #     13
# print(ch.withdraw(3))
# #     9
# ch2 = FreeChecking('John')
# ch2.balance = 10
# print(ch2.withdraw(6)) # No fee
#     # 7
# print(ch2.withdraw(5))  # ch2 doesn't charge a fee but uses a free chance
#     # 5
# print(ch2.withdraw(2))  # Not enough to cover fee + withdraw
#     # 'Insufficient funds'