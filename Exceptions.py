class NegativeNumberOfPaymentsError(Exception):
    print("The number of installments must be greater than zero")

class ZeroAmountError(Exception):
    print("The amount must be greater than zero")

class CreditCardAlreadyExists(Exception):
    print("The credit card already exists")

class CardNotFoundError(Exception):
    print("The card does not exist")