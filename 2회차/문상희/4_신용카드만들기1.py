import sys

sys.stdin = open("_신용카드만들기1.txt")

test_case = int(input())

for test_num in range(1, test_case + 1):
    card_number = list(map(int, input().split()))

    sum = 0

    for position in range(len(card_number)):
        position_num = card_number[position]
        if position % 2 == 0:
            sum += position_num * 2
        else:
            sum += position_num
    # 시작값을 0으로 가지는 sum에 홀수 자리면 2를 곱한 수를 더하고 짝수 자리면 그냥 수를 더하는 것을 반복하여
    # 15자리까지 합을 구하여 주었습니다.

    if sum % 10 == 0:
        print(f'#{test_num} 0')
    else:
        print(f'#{test_num} {10 - (sum % 10)}')
        # 16번째까지 더해서 10의 배수가 되어야 하므로 10에서 15번째까지 나눈 값에 10을 뺴주어 값을 구했는데
        # 15번째자리까지 합이 10의 배수인 경우 10이 나오므로 
        # 15번째까지 합이 0인 경우 0을 출력하게 해주고 
        # 아닌경우 10 - (sum % 10)을 출력하도록 해주었습니다.