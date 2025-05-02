class TransactionHistory:
    def __init__(self, transactions):
        self.transactions = transactions
        self.index = 0

history = TransactionHistory(["Deposit $100", "Withdraw $50", "Deposit $200"])
for transaction in history:
    print(transaction)