"""
* Flask를 이용해서, 블록체인 API를 제공 
"""
# import json
# from textwrap import dedent

from flask import Flask, jsonify, request, render_template, redirect
from uuid import uuid4

from block_class.block_chain import BlockChain


app = Flask(__name__)

# 32-bits 유니크 아이디를 생성한다 - '11864aaa-d1b2-45af-9c5a-c21dda71c6fc'
node_identifier = str(uuid4()).replace("-", "")

bc = BlockChain()


@app.route("/", methods=["GET"])
def index():
    return render_template('./chain_help.html')


@app.route("/chains", methods=["GET"])
def full_chain():
    response = {
        "chain": bc.chain,
        "length": len(bc.chain),
    }

    return jsonify(response), 200


@app.route("/mine", methods=["GET"])
def mine():
    # 마지막 블럭의 작업증명을 기준으로 POW을 계산한다 (보상100)
    last_block = bc.last_block
    last_proof = last_block["proof"]

    proof = bc.proof_of_work(last_proof)
    conpensation = 100

    bc.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=conpensation)

    previous_hash = bc.hash(last_block)
    block = bc.new_block(proof, previous_hash)

    response = {
        "message":         "... new block forged! ...",
        "index":           block["index"],
        "transactions":    block["transactions"],
        "proof":           block["proof"],
        "previous_hash":   block["previous_hash"]
    }

    return jsonify(response), 200


@app.route("/transactions/new", methods=["GET", "POST"])
def new_transaction():
    # 수신,송신,금액이 존재하면 거래를 기록하고 내용을 보여줌
    if request.method == "POST":
        # values = request.get_json()

        sender = request.form["sender"]
        recipient = request.form["recipient"]
        amount = request.form["amount"]

        values = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount}

        required = ["sender", "recipient", "amount"]

        if not all(k in values for k in required):
            return "... missing values ...", 400

        index = bc.new_transaction(
            values["sender"],
            values["recipient"],
            values["amount"])

        response = {
            "message": "... Transaction will be added to Block {0}".format(index),
            "current TX": bc.current_transactions
        }
        return jsonify(response), 201

    else:
        return render_template("./new_TX.html"), 200


@app.route("/transactions", methods=["GET"])
def show_transaction():
    # 블록에 기록하기 위해 모인, 기록 전, 거래자료를 조회한다.
    response = bc.current_transactions
    return jsonify(response), 200


@app.route("/transactions/all", methods=["GET"])
def show_transaction_all():
    # 블록체인에서 모든 거래내역만 뽑아낸다 (채굴보상은 거래제외)
    echo = bc.show_all_transaction(bc.chain)
    echo = "<pre>" + echo + "</pre>"

    return echo

@app.route("/write", methods=["GET"])
def write_chains():
    # 이제까지 모인 체인블록을 Json 화일에 기록/보관한다.
    chains = bc.write_json()
    response = {
        "chains": chains,
        "message": "...  Writing whole chains to chains.json ..."
    }
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
