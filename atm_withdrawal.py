#Create

account_balance= 1000.00
print("Welcome to the ATM!")
print("To withdraw money, please enter the amount you wish to withdraw.")
print("You can also enter -1 to cancel the transaction.")
print("Enter withdrawal amount:")
withdrawal_amount = input()
while True:
    withdrawal_amount = float(withdrawal_amount)
    
    if withdrawal_amount > account_balance:
        print("Insufficient funds. Please enter a smaller amount.")
    elif withdrawal_amount < 1000 and withdrawal_amount > 0:
        account_balance -= withdrawal_amount
        print(f"Withdrawal successful! Your new balance is: ${account_balance:.2f}")
        break
    elif withdrawal_amount == -1:
        print("Transaction cancelled.")
        break
