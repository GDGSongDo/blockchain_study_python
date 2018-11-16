"""
# Set CWD and other general configuration
"""
# print(__doc__)

import os
import sys

# '루트'와 '작업'디렉토리 설정 - for 스크립트런
HOME = "blockchain_study_python"
DIRS = os.path.dirname(__file__).partition(HOME)
ROOT = DIRS[0] + DIRS[1] + "/"
sys.path.append(ROOT)

# 스크립트런 '한글' 표시를 위한 커스텀모듈 실행
from _static.config import _script_run_utf8
_script_run_utf8.main()







if __name__ == '__main__':
    print(__doc__)
    print("HOME=", HOME)
    print("DIRS=", DIRS)
    print("ROOT=", ROOT)
