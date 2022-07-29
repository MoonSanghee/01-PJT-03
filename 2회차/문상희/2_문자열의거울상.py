import sys

sys.stdin = open("_문자열의거울상.txt")

test_case = int(input())

# 문자열을 뒤집고 'q', 'p', 'b', 'd'를 각 'p', 'q', 'd', 'b'로 변경해주기위해 
# 문자열을 뒤집은 문자를 만들고 첫자리부터 'qpbd' 확인하여 'pqdb로 바꿔주도록 먼저
# 접근을 해봤으나 시간초과가 떠서 q', 'p', 'b', 'd'를 키값으로 각 'p', 'q', 'd', 'b'
# 라는 밸류값을 가지도록 하는 딕셔너리를 만들고 뒤집은 문자열을 확인하며 딕셔너리를 통해
# 원하는 값으로 바꾸어주니 정답처리가 되었습니다.
for test_num in range(1, test_case + 1):
    change_word ={
        'q': 'p',
        'p': 'q',
        'b': 'd',
        'd': 'b'
    }
    # 각 값에 따라 변경해줄 값을 키-밸류 값으로 매칭하여 딕셔너리를 만들어 주었습니다.

    word = input()
    reverse_word = word[::-1]
    #거울을 통해 보면 문자열을 뒤집고 문자들을 뒤집어 주는게 편할것같아 먼저 문자열을 뒤집어 주었습니다.

    re_word = ''
    # 딕셔너리를 통해 나온 값으로 각 자리를 바꾸어 새로 저장해줄 빈 문자열을 만들었습니다.
    for each in reverse_word:
        if each in change_word:
            re_word += change_word[each]
            # 반복문을 통해 뒤집은 문자열을 돌면서 딕셔너리를 이용하여 문자를 바꾸어 빈 문자열에 저장하는 방법으로 출력할 문자열을 만들어 주었습니다.
               
    print(f'#{test_num} {re_word}')