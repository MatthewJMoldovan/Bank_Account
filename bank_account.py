class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0


    def display_user_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        print('\n')
        return self

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points += 200
            print(f"{self.first_name}, You've earned 200 points for enrolling! Your new balance is {self.gold_card_points} points!")
            print('\n')
        else:
            print(f"{self.first_name}, You are already a rewards member!")
            print('\n')
        return self

    def spend_points(self, points_spent):
        if points_spent <= self.gold_card_points:
            self.gold_card_points -= points_spent
            print(f"{self.first_name}, You've spent {points_spent} points! You have {self.gold_card_points} points remaining!")
            print('\n')
        else:
            print(f"{self.first_name}, You don't have enough points!")
            print('\n')
        return self


class BankAccount:

    all_accounts = []

    @classmethod
    def all_account_info(cls):
        for account in cls.all_accounts:
            print(f"Your account balance is:${account.balance}")
            print(f"Your interest rate is: {account.int_rate}%")

    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        print(f"You've deposited ${amount}! You're new balance is ${self.balance}")
        print('\n')
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
            print(f"Your new balance is ${self.balance}")
            print('\n')
        else:
            print("You have insuffucuent funds: Charging a $5 fee")
            print('\n')
        return self

    @staticmethod
    def can_withdraw(balance,amount):
        if(balance - amount) < 0:
            return False
        else:
            return True

    def display_account(self):
        print(f"Your account balance is:${self.balance}")
        print(f"Your interest rate is: {self.int_rate}%")
        print('\n')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance + (self.int_rate * self.balance))
            print(f"You've accured interest! Your new balance is ${self.balance}!")
            print('\n')
        else:
            print("You do not have a positive balance!")
            print('\n')
        return self




matt = User('Matt', 'Moldovan', 'matthewmoldovan@outlook.com', 24)
jane = User('Jane', 'Doe', 'jane.doe@gmail.com', 32)
john = User('John', 'Doe', 'johndoeisthecoolest@aol.com', 28)




# matt.display_user_info().enroll().spend_points(50).display_user_info().enroll()
# jane.enroll().spend_points(80).display_user_info()
# john.display_user_info().spend_points(40)

account_1 = BankAccount()
account_2 = BankAccount()


account_1.deposit(125).deposit(100).deposit(225).withdraw(300).yield_interest().display_account()
account_2.deposit(225).deposit(115).withdraw(47.50).withdraw(39.99).withdraw(19.99).withdraw(11.98).yield_interest().display_account()
BankAccount.all_account_info()