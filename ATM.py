class ATM:
    def __init__(self):
        self.accounts = {}  # Dictionary to store user accounts with user ID as keys
        self.current_user = None

    def create_account(self, user_id, pin, balance=0):
        if user_id in self.accounts:
            return "User ID already exists."
        self.accounts[user_id] = {"pin": pin, "balance": balance, "history": []}
        return "Account created successfully."

    def login(self, user_id, pin):
        if user_id in self.accounts and self.accounts[user_id]["pin"] == pin:
            self.current_user = user_id
            return True
        return False

    def logout(self):
        self.current_user = None

    def deposit(self, amount):
        if self.current_user and amount > 0:
            self.accounts[self.current_user]["balance"] += amount
            self.accounts[self.current_user]["history"].append(f"Deposited ${amount}")
            return f"Deposited ${amount} successfully. New balance: ${self.accounts[self.current_user]['balance']}"
        return "Please log in and enter a valid amount."

    def withdraw(self, amount):
        if self.current_user and amount > 0:
            if self.accounts[self.current_user]["balance"] >= amount:
                self.accounts[self.current_user]["balance"] -= amount
                self.accounts[self.current_user]["history"].append(f"Withdrew ${amount}")
                return f"Withdrew ${amount} successfully. New balance: ${self.accounts[self.current_user]['balance']}"
            return "Insufficient balance."
        return "Please log in and enter a valid amount."

    def transfer(self, receiver_user_id, amount):
        if self.current_user and receiver_user_id in self.accounts and amount > 0:
            if self.accounts[self.current_user]["balance"] >= amount:
                self.accounts[self.current_user]["balance"] -= amount
                self.accounts[receiver_user_id]["balance"] += amount
                self.accounts[self.current_user]["history"].append(f"Transferred ${amount} to {receiver_user_id}")
                self.accounts[receiver_user_id]["history"].append(f"Received ${amount} from {self.current_user}")
                return f"Transferred ${amount} to {receiver_user_id} successfully. New balance: ${self.accounts[self.current_user]['balance']}"
            return "Insufficient balance."
        return "Please log in and enter valid recipient and amount."

    def transaction_history(self):
        if self.current_user:
            history = self.accounts[self.current_user]["history"]
            return history
        return "Please log in to view transaction history."

    def quit(self):
        self.current_user = None
        return "Thank you for using the ATM."


# Example usage:
atm = ATM()
atm.create_account("user123", "1234")
atm.create_account("user456", "5678", 1000)

while True:
    print("\nOptions:")
    print("1. Login")
    print("2. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        user_id = input("Enter your user ID: ")
        pin = input("Enter your PIN: ")
        if atm.login(user_id, pin):
            while True:
                print("\nAccount Menu:")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Transfer")
                print("4. Transaction History")
                print("5. Logout")
                sub_choice = input("Choose an option: ")

                if sub_choice == "1":
                    amount = float(input("Enter the amount to deposit: "))
                    print(atm.deposit(amount))

                elif sub_choice == "2":
                    amount = float(input("Enter the amount to withdraw: "))
                    print(atm.withdraw(amount))

                elif sub_choice == "3":
                    receiver_user_id = input("Enter the recipient's user ID: ")
                    amount = float(input("Enter the amount to transfer: "))
                    print(atm.transfer(receiver_user_id, amount))

                elif sub_choice == "4":
                    history = atm.transaction_history()
                    if isinstance(history, list):
                        print("\nTransaction History:")
                        for entry in history:
                            print(entry)
                    else:
                        print(history)

                elif sub_choice == "5":
                    atm.logout()
                    break

        else:
            print("Invalid user ID or PIN.")

    elif choice == "2":
        print(atm.quit())
        break

    else:
        print("Invalid choice. Please choose a valid option.")
