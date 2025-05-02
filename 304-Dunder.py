class TransactionHistory:
    def __init__(self, transactions):
        self.transactions = transactions
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.transactions):
            raise StopIteration
        transaction = self.transactions[self.index]
        self.index += 1
        return transaction

history = TransactionHistory(["Deposit $100", "Withdraw $50", "Deposit $200"])
for transaction in history:
    print(transaction)