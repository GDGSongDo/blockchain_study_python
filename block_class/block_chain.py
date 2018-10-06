"""
* 블록체인 구현 (블록생성, 트랜잭션, 작업증명, 마이닝)
* https://goo.gl/M6XU5v
"""
import os
import hashlib
import json
from time import time
from uuid import uuid4


DIRS = os.path.dirname(__file__).partition("block_chain_study\\")
ROOT = DIRS[0] + DIRS[1]
FILE_W_DIR = ROOT + "/block_class/chains.json"


class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        if os.path.exists(FILE_W_DIR):
            # if exist, read from chains.json
            with open(FILE_W_DIR, "r") as f:
                self.chain = json.load(f)
        else:
            # if not, make Genesis block, from the scratch.
            self.new_block(proof=100, previous_hash=1)

    def new_block(self, proof, previous_hash=None):
        # Creates a new Block and adds it to the chain
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "transactions": self.current_transactions,
            "proof": proof,
            "previous_hash": previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []
        self.chain.append(block)

        return block

    def new_transaction(self, sender, recipient, amount, hash=0):
        """ Creates a new transaction to go into the next mined Block
        : param sender: <str> Sender의 주소
        : param recipient: <str> Recipient의 주소
        : param amount: <int> Amount
        : return: <int> 이 거래를 포함할 블록의 index 값
        """

        if hash:
            sender = self.hash(sender)
            recipient = self.hash(recipient)

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # Hashes a Block ... malfuntion with sort_keys=True option
        # block_string = json.dumps(block, sort_keys=True).encode()
        block_string = json.dumps(block).encode()
        return hashlib.sha256(block_string).hexdigest()

    @staticmethod
    def valid_proof(last_proof, proof):
        # arg. of SHA256() should be binary ("".encode()) ... 64 bits
        guess = str(last_proof * proof).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        # mining is to find a hash starting with difficulty (consecutive zeros)
        difficulty = "0000"
        return guess_hash[:len(difficulty)] == difficulty

    @property
    def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    def write_json(self):
        with open("./block_class/chains.json", "w") as f:
            json.dump(self.chain, f)
        return self.chain

    def show_all_transaction(self, chains):
        echo = ""
        for n in range(len(chains)):

            # 블럭 마이닝 보상거래 1개 이상의 거래가 존재 할 경우
            if len(chains[n]['transactions']) > 1:
                echo += "\n\n------ index.%s / [%s] -------"%(
                    chains[n]['index'],
                    len(chains[n]['transactions'])-1)

                for m in range(len(chains[n]['transactions'])):

                    # 마이닝 보상거래는 출력에서 제외 (보상: sender="0")
                    if chains[n]['transactions'][m]['sender'] is "0":
                        pass

                    else:
                        echo += "\
                            \n* Sender   = {0} \
                            \n* Recipent = {1} \
                            \n* Amount   = {2:,}\n".format(
                            chains[n]['transactions'][m]['sender'],
                            chains[n]['transactions'][m]['recipient'],
                            int(chains[n]['transactions'][m]['amount']),)

            else:
                echo += "\n\n... index : %s ... NO TRANSACTIONS IN THIS LEDGER!\
                        \n      (ONLY MINNING CONPENSATION or NOT)..." % (n + 1)

        return echo


if __name__ == '__main__':
    from pprint import pprint

    # 오브젝트 선언하는 순간, 최최의 Genesis Block을 생성한다
    bc = BlockChain()

    pprint(bc.chain[-1])
    input("\n... 제네시스 블럭생성 ...\n\n\n")


    # 제네시스 블록을 해쉬해서 다음블록에 기록한다.
    blocks_hashed = bc.hash(bc.chain[-1])
    print ("\n... 젠블록에 해쉬함수 적용 / 길이 = {1} bits\
            \n{0} \n\n\n".format(blocks_hashed,len(blocks_hashed)))


    # 블록과 블록사이에서, 2개의 트랜젝션이 발생한다.
    bc.new_transaction(sender='Scrouge', recipient='Alice', amount=200, hash=0)
    bc.new_transaction(sender='Alice', recipient='Bob', amount=150, hash=0)
    pprint(bc.current_transactions)
    input("\n... 트랜잭션 2개 발생 ...\n\n\n")


    # 새로운 블럭이 발생하면, 이전블록 해쉬와 거래정보가 자동으로 기록된다.
    bc.new_block(proof=100)
    pprint(bc.chain)
    input("\n... 새로운 블럭생성(마이닝)...\
        \n... 자동으로 트랜젝션과 이전해쉬가 기록 (가독성을 위해 해쉬변환 생략) ...\
        \n\n\n")


    # 이전 블록정보를 해쉬한다 (마지막 블럭정보)
    blocks_hashed = bc.hash(bc.chain[-1])
    print ("\n... 이전블록에 해쉬함수 적용 / 길이 = {1} bits\
    \n{0} \n\n\n".format(blocks_hashed,len(blocks_hashed)))


    # 블록과 블록사이에서, 새로운 1개의 트랜젝션이 발생한다.
    bc.new_transaction(sender='Scrouge', recipient='Charlie', amount=1000, hash=0)
    pprint(bc.current_transactions)
    input("\n... 트랜잭션 1개 발생 ...\n\n\n")


    # 새로운 블록이 생성되면, 그동안 발생한 거래와 이전블럭 해쉬를 자동으로 기록한다.
    bc.new_block(proof=100)
    pprint(bc.chain)
    input("\n... 새로운 블럭생성(마이닝)...\
        \n... 자동으로 트랜젝션과 이전해쉬가 기록 (가독성을 위해 해쉬변환 생략) ...\
        \n\n\n")
