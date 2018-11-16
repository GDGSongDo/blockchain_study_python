"""
* difficulty 가 올라 갈수록 난이도가 높아진다 (발견 할 확률이 작아 짐?)
* 942,344 회 반복 만에, 앞자리 '00000'에 일치 하는 해쉬를 찾아 냄
* '0' 반복이 작을수록 빠르게 찾아 낼 수 있다 (작은 반복)
*
* 0 = 10 회
* 00 = 532 회
* 000 = 5,089 회
* 0000 = 73,571 회
* 00000 = 942,344 회
"""
print(__doc__)

import hashlib


def valid_proof(last_proof, nonce):
    # sha256 함수는 바이너리 스트링을 받는다. encode()= b''
    guess = str(last_proof * nonce)
    hashed_guess = hashlib.sha256(guess.encode()).hexdigest()
    difficulty = "000000"
    result_bool = hashed_guess[:len(difficulty)] == difficulty
    return (result_bool, guess, hashed_guess)


def proof_of_work(last_proof):
    nonce = 0
    while valid_proof(last_proof, nonce)[0] is False:
        nonce += 1
        guess = valid_proof(last_proof, nonce)[1]
        hashed_guess = valid_proof(last_proof, nonce)[2]
        print(guess, hashed_guess)
    return nonce


if __name__ == '__main__':
    last_proof = 111
    print(proof_of_work(last_proof))



"""
b'104599851' 61fff6b461bd432e1b9f0980c4e244c8e7b2528a7ae1160124f0cbc4cb33613e
b'104599962' 024fcb60c15c6c34bd835ac2abd515f859d249b15e509d9061243bad1c98669e
b'104600073' d43349a434579afcf5bc16d46ee24811e10b880d8dd55dd9183a2f159a8e6bb5
b'104600184' 000009ddc25ce76342c3658040ae60f68f8ad8fa80b97ba7fada45cedc6f5c75
942344

Process returned 0 (0x0)        execution time : 78.072 s
계속하려면 아무 키나 누르십시오 . . .
"""
