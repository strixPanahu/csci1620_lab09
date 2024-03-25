# **LAB 09**


## **SUBMISSION INSTRUCTIONS***

- [x] 0.) Submit | python file using the naming convention below:
	* accounts.py


## **QUESTION**

- [ ] 1.) Inside accounts.py, create a class named Account with the methods below.

	- [ ] a.) def init__(self, name, balance=0):

		- [ ] i.) This should be used to set the default values for each account object.

		- [ ] ii.) It should contain 2 private variables (account_name, account_balance), that should hold the account name and a balance respectively. Example:
			* account_one =Account(‘John’) is an account object whose account_name =John and account_balance =0.
			* account_two =Account(‘Tom’, 30) is an account object whose account_name =Tom and account_balance =30.
			* account_three =Account(‘Tim’, -300) is an account object whose account_name =Tim and account_balance =0.

		- [ ] iii.) After setting the account_balance, call the set_balance method to check that the account balance is a valid value.

	- [ ] b.) def deposit(self, amount):

		- [ ] i.) This should increase the account balance by the specified amount.

		- [ ] ii.) If the amount is a negative number or0, nothing should happen to the account balance (since you cannot deposit a negative amount of money or $0).

		- [ ] iii.) Return the Boolean value True if the deposit transaction is successful and False if the transaction is unsuccessful (didn’t change account balance).

	- [ ] c.) def withdraw(self, amount):

		- [ ] i.) This should decrease the account balance by the specified amount.

		- [ ] ii.) If the amount is a negative number, 0, or more than the current account balance, nothing should happen to the account balance (since you cannot withdraw a negative amount, $0, and you cannot withdraw more than your current account balance).

		- [ ] i.) Return the Boolean value True if the deposit transaction is successful and False if the transaction is unsuccessful (didn’t change account balance).

	- [ ] d.) def get_balance(self):

		- [ ] i. This should return the account balance.

	- [ ] e.) def get_name(self):

		- [ ] i. This should return the account name.

	- [ ] f.) def set_balance(self, value):

		- [ ] i.) This should set the account balance to the value provided.

		- [ ] ii.) Please note, if the value is less than 0, set the account balance to 0 instead.

	- [ ] g.) def set_name(self, value):

		- [ ] i.) This should set the account name to the value provided.
 
	- [ ] h.) def __str__ (self):

		- [ ] i.) This should return the account details (use getter methods where applicable).

		- [ ] ii.) Check main.py for the format of the string to be returned. 


- [ ] 2.) Inside accounts.py, create another class named SavingAccount with the variables and methods below (SavingAccount should be designed as a child of Account).

	- [ ] a.) MINIMUM:

		- [ ] i.) This should be a class variable whose initial value is 100 ($100).

		- [ ] ii.) This is the minimum balance the account can have at any one point.

	- [ ] b.) RATE:

		- [ ] i.) This should be a class variable whose initial value is 0.02 (2%).

		- [ ] ii.) It’s the interest rate to be applied to the account balance when applicable.

	- [ ] c.) def __init__(self, name):

		- [ ] i.) This should be used to set the default values for each saving account object.

		- [ ] ii.) It should contain a private variable to keep track of the number of deposits made in the account (deposit_count)

		- [ ] iii.) Example: account_two =SavingAccount(‘Jane') is a savings account object whose account_name =Jane, account_balance = 100, and deposit_count =0.

	- [ ] d.) def apply_interest(self):

		- [ ] i.) This should apply a 2% interest rate to the account balance for every 5 deposits made on the account (if someone deposits $100 5 times, on the 5 deposit their account balance would be $612 instead of$600 —since they started off with $100 in their account at the time of creation).

	- [ ] e.) def deposit(self, amount):

		- [ ] i.) This should increase the account balance by the specified amount.

		- [ ] ii.) If the amount is a negative number or 0, nothing should happen to the account balance (since you cannot deposit a negative amount of money or $0).

		- [ ] iii.) You need to check whether it’s appropriate to apply an interest based off the number of deposits made.

		- [ ] iv.) Return the Boolean value True if the deposit transaction is successful and False if the transaction is unsuccessful (didn’t change account balance).

	- [ ] f.) def withdraw(self, amount):

		- [ ] i.) This should decrease the account balance by the specified amount.

		- [ ] ii.) If the amount is a negative number, 0, or reduces the account balance to an amount less than the minimum, nothing should happen to the account balance.

		- [ ] iii.) Return the Boolean value True if the withdraw transaction is successful and False if the transaction is unsuccessful (didn’t change account balance).

	- [ ] g.) def get_balance(self):

		- [ ] i. This should return the account balance.

	- [ ] h.) def get_name(self):

		- [ ] i. This should return the account name.

	- [ ] i.) def set_balance(self, value):

		- [ ] i.) This should set the account balance to the value provided.

		- [ ] ii.) Please note, if the value is less than the account minimum, set the account balance to the account minimum instead.

	- [ ] j.) def set_name(self, value):

		- [ ] i. This should set the account name to the value provided.

	- [ ] k.) def__str__(self):

		- [ ] i.) This should return the account details.

		- [ ] ii.) Check main.py for the format of the string to be returned.


- [ ] 3.) Test if the code in the accounts.py file works as expected by downloading main.py to the same location accounts.py is located and then run main.py. The output you get should correspond to that in the comments found in main.py. If you get different values, it means that you need to work on the logic of the methods in the accounts.py file.


- [ ] 4.) Please note: You must use inheritance where applicable (there are points awarded for this 1.e., don’t repeat code that already exists in the parent class).

	- [ ] a.) Use the variable and method names provided.

	- [ ] b.) Don’t introduce any new variables or methods.
