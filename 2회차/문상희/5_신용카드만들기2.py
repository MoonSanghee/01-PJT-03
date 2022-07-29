import sys

sys.stdin = open("_신용카드만들기2.txt")

# 카드번호가 성립하려면 '-'를 뺀 번호의 길이가 16자리이고 맨 처음 자리가 3, 4, 5, 6, 9
# 여야하기때문에 먼저 '-'가 들어갔으면 '-'를 빼고 숫자로만 이루어지게 만들고 길이가 16자리이고
# 맨앞자리가 3,4,5,6,9인 두 조건을 다 충족하는 경우를 찾는 방법으로 답을 구하였습니다.

test_case = int(input())
check_list = [3, 4, 5, 6, 9]
# 앞자리를 비교할 때 쓸 앞자리 숫자들이 모인 리스트를 만들어 주었습니다

for test_num in range(1, test_case + 1):
    card_number = input()
    # -가 포함된 경우도 있어 문자열형태로 입력값을 받았습니다.
    checked = ''
    for position in range(len(card_number)):
        if card_number[position] != '-':
            checked += card_number[position]
    # 문자열을 순회하며 '-'이 아닌경우 각 자릿값을 빈 문자열에 넣어주어 '-'을 제거한 문자열을 구하였습니다.

    if int(card_number[0]) in check_list and len(checked) == 16:
        # 입력값을 문자열로 받았기 때문에 첫자리를 정수형으로 변환하여 체크리스트와 비교해주었습니다.
        print(f'#{test_num} 1')
    else:
        print(f'#{test_num} 0')