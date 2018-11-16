"""
# 마이닝시 보상이 발생하므로, 매 블럭 거래정보 있음
# 블럭정보.json 를 읽어서, 거래 정보를 추출한다.
#
"""
print(__doc__)


import os
import sys
import json
from pprint import pprint

# '루트'와 '작업'디렉토리 설정 - for 스크립트런
HOME = "blockchain_study_python"
DIRS = os.path.dirname(__file__).partition(HOME)
ROOT = DIRS[0] + DIRS[1] + "/"
sys.path.append(ROOT)

# 스크립트런 '한글' 표시를 위한 커스텀 모듈 실행
from _static.config import _script_run_utf8
_script_run_utf8.main()


# BLOCK_INFO.JSON TO SHOW INSIDE of TX
# FILE_W_DIR = ROOT + "_static/json/block.json"
FILE_W_DIR = ROOT + "_static/json/chains_old.json"


def get_json(file_w_dir):
    with open(file_w_dir, mode='r') as f:
        chains = json.load(f)
    return chains


def show_transaction(chains):
    for n in range(len(chains)):

        # 블럭 마이닝 보상거래 1개 이상의 거래가 존재 할 경우
        if len(chains[n]['transactions']) > 1:
            print("\n\n------ index.%s / [%s] -------" %(
                chains[n]['index'],
                len(chains[n]['transactions'])-1),
                end="")

            for m in range(len(chains[n]['transactions'])):

                # 마이닝 보상거래는 출력에서 제외 (보상: sender="0")
                if chains[n]['transactions'][m]['sender'] is "0":
                    pass

                else:
                    print("\
                        \n* Sender   = {0} \
                        \n* Recipent = {1} \
                        \n* Amount   = {2:,}".format(
                        chains[n]['transactions'][m]['sender'],
                        chains[n]['transactions'][m]['recipient'],
                        int(chains[n]['transactions'][m]['amount']),)
                    )
        else:
            print("\n\n... index : %s ... NO TRANSACTIONS IN THIS LEDGER!\
                    \n      (ONLY MINNING CONPENSATION or NOT)..." % (n + 1))



if __name__ == '__main__':
    # json 에서 전체 체인정보를 읽어온다.
    chains = get_json(FILE_W_DIR)

    # 전체 json 정보를 출력해서 확인한다
    # pprint(chains)

    # 체인에서 거래정보만 추출해서 보여준다 (블럭보상은 제외 함)
    show_transaction(chains)
