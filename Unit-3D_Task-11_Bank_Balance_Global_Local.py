# Global bank balance
balance = 1000

# Function to deposit money
def deposit(amount):
    global balance
    balance += amount
    print("Deposited Amount: ₹", amount)
    print("Updated Balance: ₹", balance)

# Function using local balance
def local_balance():
    balance = 500
    print("Local Balance: ₹", balance)

# Display original balance
print("Original Balance: ₹", balance)

# Deposit money
deposit(500)

# Display local balance
local_balance()

# Display actual bank balance
print("Final Bank Balance: ₹", balance)