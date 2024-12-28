class NegativeDepositError(Exception):
    pass

deposit_amount = float(input("Enter the deposit amount: "))
if deposit_amount < 0:
    raise NegativeDepositError("Deposit amount cannot be negative.")
else:
    print(f"Deposit of {deposit_amount} successful.")
