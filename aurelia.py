import hashlib as hash

class AureliaBlock:

    def __init__(self, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.transactions = transactions
        
        self.block_data = self.previous_hash + "-".join(self.transactions)
        self.block_hash = hash.sha256(self.block_data.encode()).hexdigest()

        print("Previous Hash: " + self.previous_hash)
        print("Transactions: " + str(self.transactions))
        print("Current Hash: " + self.block_hash)
        print(" ")

t1 = "First transaction!"
t2 = "Second transaction"
t3 = "Third transaction"
t4 = "Fourth transaction"
t5 = "Fifth transaction"
t6 = "Sixth transaction"

initial_block = AureliaBlock("First hash!", [t1, t2])

second_block = AureliaBlock(initial_block.block_hash, [t3, t4])

third_block = AureliaBlock(second_block.block_hash, [t5, t6])