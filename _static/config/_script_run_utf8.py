""" make stdout environment cp494 to utf-8 [WINDOWS-7]
  1.BEFORE: 안녕세계 = �ȳ缼��
    - sys.getdefaultencoding() = utf-8
    - sys.stdout.encoding = cp949        ---> change to 'utf-8'

  2.AFTER: 안녕세계 = 안녕세계
    - sys.getdefaultencoding() = utf-8
    - sys.stdout.encoding = 'utf-8'
"""
# print(__doc__)

import io
import sys


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


""" if __name__ 로 경계를 치면, 외부 모듈호출 때 자체 실행을 방지한다. """
if __name__ == '__main__':
    _ = """*** _script_run_utf8 스크립트의 용도 :
    -------------------------
     - ATOM 에디터 '스크립트런' 실행 시, 한글인코딩 깨지는 문제 해결
     - 실행방법 : 모듈 임포트/메인 실행 (sys.stdout, std.err을 utf8로 변경)
         mport _script_run_utf8
         script_run_utf8.main()


     - 실행 후 변경사항 :
      stdout, stderr 환경을 'cp494'에서 'utf-8'로 변경 한다.

      1.BEFORE: 안녕세계 = �ȳ缼��
        - sys.getdefaultencoding() = utf-8
        - sys.stdout.encoding = cp949        ---> change to 'utf-8'

      2.AFTER: 안녕세계 = 안녕세계
        - sys.getdefaultencoding() = utf-8
        - sys.stdout.encoding = 'utf-8'

    """
    print('\n' + _)
    main()
