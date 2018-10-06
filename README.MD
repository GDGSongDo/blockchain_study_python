---
language : python, html
labrary : flask
---

<br><br>
### 0. INTRO 👋

This is not for project, but for the own personal study, the better understanding how blockchain work in simple way.
Thus, please just refer it as one of many sample materials.



<br><br>
### 1. HOW TO RUN

Run bash window on the target folder and type in 'python server.py'. Then the first block, index 1, will be automatically generated if there is no stored history file named **chain.json**.

regarding **chain.json** file, there's no chain.json at first. it is generated only if you like to. (I prepare 'write' menu on webpage)

When '**chain.json**', a written history file, exists, the block history will be restored autonomously. To avoid at first, I changed the file name to '**chain_old.json**', which has the several depth of block history.

![bash_run image](/_static/bash_run.png)



<br><br>
### 2. HOW IT SHOWS

> 'http://localhost:5000' in browser

![main_screen](/_static/chain_help.png)




<br><br>
### 3. ABOUT JSON
In block_class, there're 3 jason files.

> 1. **blcok.json** - the first intention, but to many hashs
> 2. **chains_old.json** - already described on the top.
> 3. **genesis.json** - Ethurium genesis block format, just refer to it

This it not exact as it can be, but just alludes coinbase transaction. Because it is compensation for mining, sender is nobody, recipient is randomly generated node ID and amount is set as 100, form of variable for mining reward.

<pre>
    {
     "sender": "0",
     "recipient": "17460cdf96bc403ca792bf08a7f87d4d",
     "amount": 100
    }
</pre>

![dir_structure](/_static/structures.png)



<br><br>
### 4. OTHERS
> As a beginner trying to bite a little dent on learning the blockchain technology, other constructive opinoins are always welcomed and let's make it together! 😏




<br><br>
### 5. REFERENCES
> 1. 블록체인 구현 (블록생성, 트랜잭션, 작업증명, 마이닝) -  https://goo.gl/M6XU5v
> 2. 파이썬으로 블록체인 개발 ( 아직 Part1밖에 없음) : https://goo.gl/V2owrp
