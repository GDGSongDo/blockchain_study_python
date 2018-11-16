"""
# 우연히 첫자리가 '000000'으로 시작하는 해쉬를 발견 했을 때, nonce값 찾음
# 목표 타겟해쉬값 (000000...)을 찾을때 까지 논스값을 1씩 증가 반복계산 한다.
# 중간과정 Print생략, 빠르게 탐색(6자리)결과 = '000000..' 약 85.6초 소요.
# 목표난이도의 타겟 해쉬값을 찾았을 때, nonce값이 작업증명(POW).
# nonce를 발견하는 시간, 타임스템프와 현재해쉬 값을 별도로 (추가)저장한다.
# 원래는, 앞자리 0은 생략되기 때문에 Reverse 해쉬값, 뒤집어서 저장 (생략)
"""
# print(__doc__)


import time

from pprint import pprint
from hashlib import sha256

MINING_UID = 'node_identifier_uid'

TRANSACTIONS = [
        {
            'sender': 'Alice',
            'recipient': 'Bob',
            'amount': 1000
        },
        {
            'sender': 'Scrouge',
            'recipient': 'Alice',
            'amount': 800
        },
        {
            'sender': 'coinbase_reward',
            'recipient': MINING_UID,
            'amount': 200
        },
    ]


block = {
        'index': 12,
        'difficulty': '000000',
        'nonce': 0,
        'hash_previous': '000000ea8482b821aff9b2ce6103f69e',
        'transaction': TRANSACTIONS,
    }


def get_hash_w_nonce(block, nonce):
    """ 최근 블럭에 Nonce를 대입하여 해쉬값을 리턴한다"""
    block['nonce'] = nonce
    hash = sha256(str(block).encode()).hexdigest()
    return hash


def add_header(block, block_hash):
    """ Block Header에 Time-stamp와 계산 된 블럭해쉬를 기록"""
    header = {
        'timestamp': time.time(),
        'hash_present': block_hash, }
    for _key, _val in header.items():
        block[_key] = _val
    return block


def proof_of_work(block):
    nonce = 0
    difficulty = block['difficulty']

    while True:
        hash = get_hash_w_nonce(block, nonce)

        if hash[:len(difficulty)] == difficulty:
            hash_present = hash[:32]
            add_header(block, hash_present)
            return block
        nonce += 1


if __name__ == '__main__':
    block = proof_of_work(block)
    pprint(block)





"""
{'difficulty': '000000',
 'hash_present': '00000028d6b3e712a4f06ff5263b5d2b',
 'hash_previous': '000000ea8482b821aff9b2ce6103f69e',
 'index': 12,
 'nonce': 11646076,
 'timestamp': 1541669896.3479497,
 'transaction': [{'amount': 1000, 'recipient': 'Bob', 'sender': 'Alice'},
                 {'amount': 800, 'recipient': 'Alice', 'sender': 'Scrouge'},
                 {'amount': 200,
                  'recipient': 'node_identifier_uid',
                  'sender': 'coinbase_reward'}]}

Process returned 0 (0x0)        execution time : 85.600 s
계속하려면 아무 키나 누르십시오 . . .
"""
