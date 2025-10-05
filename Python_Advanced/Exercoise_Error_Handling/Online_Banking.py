class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass


def bank_account(pin_code, balance, age):
    while (command := input()) != 'End':
        try:
            if command.startswith('Send Money'):
                command_type, money_string, entered_pin = command.split('#')
                money = float(money_string)
                if age < 18:
                    raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
                if entered_pin != pin_code:
                    raise PINCodeError("Invalid PIN code")
                if money > balance:
                    raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

                balance -= money
                print(f"Successfully sent {money:.2f} money to a friend")
                print(f"There is {balance:.2f} money left in the bank account")

            elif command.startswith('Receive Money'):
                command_type, money_string = command.split('#')
                money = float(money_string)

                if money < 0:
                    raise MoneyIsNegativeError("The amount of money cannot be a negative number")

                added = money / 2
                balance += added
                print(f"{added:.2f} money went straight into the bank account")
            else:
                print('Invalid command')
        except Exception as err:
            print(err)

user_data = input().split(", ")
pin_code = user_data[0]
balance = float(user_data[1])
age = int(user_data[2])

bank_account(pin_code, balance, age)
