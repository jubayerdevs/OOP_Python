class BankAccount:
  #   __balance = 0   #  (_) means protected (__) means private
  #  name = ""

    def __init__(self, balance, name):
        self.__balance = balance
        self.name = name

    def print_balance(self):
        print(f"The current balance is {self.__balance}")


    def set_balance(self, user, new_balance):
        if new_balance < 500:
            print("Not Allowed")
        else:
            print(f"User {user} updated the balance to {new_balance}")
            self.__balance = new_balance


new_acc = BankAccount(5000, "Mr. X")
new_acc.print_balance()

new_acc.set_balance("Banker", 2000)
new_acc.print_balance()


# new_acc = BankAccount()
# new_acc.balance = 5000
# new_acc.name = "Mr. Y"

# print(new_acc.balance)