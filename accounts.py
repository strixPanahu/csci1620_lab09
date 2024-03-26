"""
    CSCI 1620 001/851
    Professor Owora
    Week 09 - Lab 09
    25/03/2024

    https://github.com/strixPanahu/csci1620_lab09
"""


class Account:
    def __init__(self, name, balance=0):
        """
        Customer account with Name & Balance. Initial balance defaults to policy minimum, if Balance is insufficient
        :param name: Customer Name (String)
        :param balance: Initial Balance (+float); if invalid value provided, defaults to policy Minimum
        """
        self._account_name = None
        self._account_balance = None

        self.set_name(name)
        self.set_balance(balance)

        if balance != self.get_balance():
            print("Error setting balance of " + str(balance) + "; defaulted to " + str(self.get_balance()))

    def deposit(self, amount):
        """
        Increase total value of Balance
        :param amount: Currency addend (+float)
        :return: True/False successful deposit
        """
        if amount > 0:
            self.set_balance(self.get_balance() + float(amount))
            return True
        else:
            return False

    def withdraw(self, amount):
        """
        Decrease total value of Balance
        :param amount: Currency subtrahend (+float); difference must be greater than policy Minimum
        :return: True/False successful deposit
        """
        if 0 < amount <= self.get_balance():
            self.set_balance(self.get_balance() - float(amount))
            return True
        else:
            return False

    def get_balance(self):
        return self._account_balance

    def get_name(self):
        return self._account_name

    def set_name(self, value):
        self._account_name = str(value)

    def set_balance(self, value):
        """
        Define total account Balance
        :param value: Value in currency (+float); set to default if less than policy Minimum
        """
        if value > 0:
            self._account_balance = float(value)
        else:
            self._account_balance = 0

    def __str__(self):
        """
        User-friendly formatting of Name & Balance
        :return: Format: "Account name = Jessie Smith, Account balance = 999"
        """
        return "Account name = " + str(self.get_name()) + ", Account balance = " + str(f"{self.get_balance():.2f}")


class SavingAccount(Account):
    MINIMUM = 100
    RATE = .02

    def __init__(self, name):
        super().__init__(name)

        self._account_name = None
        self._account_balance = None

        self.set_name(name)
        self.set_balance(self.MINIMUM)
        self._deposit_count = 0

        if self.MINIMUM != self.get_balance():
            print("Error setting balance of " + str(self.MINIMUM) + "; defaulted to " + str(super().get_balance()))

    def apply_interest(self):
        """
        Updates Balance to the product of original Balance as multiplicand and (1 + RATE) as multiplier
        """
        self.set_balance(super().get_balance() * (1 + self.RATE))

    def deposit(self, amount):
        if super().deposit(amount):
            self._deposit_count += 1
            if self._deposit_count == 5:
                self.apply_interest()
                self._deposit_count = 0

            return True
        else:
            return False

    def withdraw(self, amount):
        minimum_balance = amount + self.MINIMUM
        if self.MINIMUM <= minimum_balance <= super().get_balance():
            super().withdraw(amount)
            return True
        else:
            return False

    def get_balance(self):
        return super().get_balance()

    def get_name(self):
        return super().get_name()

    def set_name(self, value):
        super().set_name(value)

    def set_balance(self, value):
        if value > self.MINIMUM:
            super().set_balance(value)
        else:
            super().set_balance(self.MINIMUM)

    def __str__(self):
        return "SAVING ACCOUNT: " + super().__str__()
