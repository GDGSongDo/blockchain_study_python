import re

FROM_SCRIPT = '__script.txt'
TO_MOD_SCRIPT = '__modified_script.txt'


with open(FROM_SCRIPT, mode='r', encoding='utf-8') as f:
    CONTENTS_WHOLE = f.read()        # 오브젝트를 사용하면, 메모리에서 지워짐.


def get_matched_list(script_str, regex_str):
    """ 정규표현식 오브젝트 생성(계속 사용) """
    """ 정규표현식 오브젝트와 매칭되는 리스트 반환한다 (findall 객체) """
    p = re.compile(regex_str, re.MULTILINE)
    matched_list = p.findall(script_str)         # list of matched
    return matched_list


def get_appended_list(origin_list, front_str="", rear_str=""):
    """ 매칭된 리스트에서 하나씩 불러내서 문자를 추가한다 """
    list_modified = []
    for n, item in enumerate(origin_list, 0):
        list_modified.append(front_str + item + rear_str)
    return list_modified


def get_changed_strings(origin_strs, origin_list, changed_list):
    """ 검색 리스트와 변경리스트를 받아서, 원문에서 교체시켜준다 """
    changed_strs = origin_strs
    for n, item in enumerate(origin_list, 0):
        changed_strs = changed_strs.replace(origin_list[n], changed_list[n])
    return changed_strs.strip()


def show_count_list(find_list):
    """ 검색 된 타임스템프(리스트 갯수) 확인 사살 """
    print(find_list, end="\n .... Find %s matches!\n\n\n" % len(find_list))


def main():
    # 정규표현식과 매칭되는 단어를 리스트로 뽑아준다 -- 여기서는 타임스템프 표현
    times_matched = get_matched_list(CONTENTS_WHOLE, '[0-9]+:[0-9][0-9]')

    # 타임스탬프 리스트에 앞뒤로 스트링을 추가한다 -- 여기서는 앞 줄바꿈 만
    times_modified = get_appended_list(times_matched, "\n", "")

    # 두 리스트의 내용을 카운트해서 비교해 본다 -- 귀찮다, 끄자!
    # show_count_list(times_matched)
    # show_count_list(times_modified)

    # 오리지날 스트링에서 오리지날 매칭리스트와 변경 리스트를 참조해서 내용을 교체한다
    changed_content = get_changed_strings(
        CONTENTS_WHOLE, times_matched, times_modified)

    # 제대로 변경되었는지 변경내용 echo를 뿌려준다 -- 귀찮거나, 필요없으면 생략!
    # print(changed_content)

    # 변경된 내용을 'TO_MOD_SCRIPT' 에 화일로 기록한다
    with open(TO_MOD_SCRIPT, mode='w', encoding='utf-8') as f:
        f.write(changed_content)


if __name__ == '__main__':
    main()
