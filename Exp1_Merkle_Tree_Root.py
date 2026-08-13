import hashlib

def build_merkle_tree(transactions):
    if len(transactions) == 0:
        return None

    # Hash all transactions first
    transactions = [
        hashlib.sha256(tx.encode('utf-8')).hexdigest()
        for tx in transactions
    ]

    if len(transactions) == 1:
        return transactions[0]

# Recursive construction of the Merkle Tree
    while len(transactions) > 1:

        if len(transactions) % 2 != 0:
            transactions.append(transactions[-1])

        new_transactions = []

        for i in range(0, len(transactions), 2):
            combined = transactions[i] + transactions[i + 1]
            hash_combined = hashlib.sha256(combined.encode('utf-8')).hexdigest()

            print("Combined Hash:", hash_combined)

            new_transactions.append(hash_combined)

        transactions = new_transactions

    return transactions[0]


transactions = [
    "Alice -> Bob : $200",
    "Bob -> Dave : $500",
    "Dave -> Eve : $100",
    "Eve -> Alice : $300",
    "Roo -> Bob : $50"
]

merkle_root = build_merkle_tree(transactions)

print("Merkle Root:", merkle_root)


