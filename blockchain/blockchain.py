import hashlib
import json
import time

class Block:
    def __init__(self, index, data, timestamp, previous_hash):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Krijon një hash unik për bllokun duke përdorur të gjitha atributet.
        """
        block_string = json.dumps({
            'index': self.index,
            'data': self.data,
            'timestamp': self.timestamp,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        """
        Simulon Proof of Work: minon bllokun derisa hash-i fillon me 'difficulty' numër të zero-ve.
        """
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Blloku {self.index} u minua: {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 10

    def create_genesis_block(self):
        """
        Krijon bllokun e parë të zinxhirit, i njohur si Genesis Block.
        """
        return Block(0, "Genesis Block", time.time(), "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Shton një bllok të ri në zinxhir duke siguruar që lidhja me bllokun e mëparshëm është e saktë.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Verifikon integritetin e të gjithë zinxhirit të blloqeve.
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Kontrollon nëse hash-i i bllokut është i saktë
            if current.hash != current.calculate_hash():
                print(f"Gabim në hash për bllokun {i}")
                return False

            # Kontrollon lidhjen me bllokun e mëparshëm
            if current.previous_hash != previous.hash:
                print(f"Gabim në lidhjen me bllokun e mëparshëm për bllokun {i}")
                return False
        return True

if __name__ == "__main__":
    # Krijon një instancë të blockchain-it
    my_blockchain = Blockchain()

    # Shton disa blloqe per demonstrim
    print("Shtimi i bllokut 1...")
    my_blockchain.add_block(Block(1, {"amount": 4}, time.time(), ""))

    print("Shtimi i bllokut 2...")
    my_blockchain.add_block(Block(2, {"amount": 10}, time.time(), ""))

    # Verifikon nëse zinxhiri është i integruar
    print("A është zinxhiri valid?", my_blockchain.is_chain_valid())
