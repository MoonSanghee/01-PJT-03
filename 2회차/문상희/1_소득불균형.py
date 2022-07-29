import sys

sys.stdin = open("_소득불균형.txt")

test_case = int(input())

# 주어지는 소득과 인원수를 이용하여 평균을 구하고 리스트에서 평균값 이하의 수입을 가지는
# 사람이 나올때마다 0에 값을 더해주는 방식으로 접근하였습니다.

for test_num in range(1, test_case + 1):
    people = int(input())
    income = list(map(int, input().split()))
    # 첫번째 주어지는 정수를 사람수
    # 두번째 띄워쓰며 주어지는 값들을 각 사람의 수입이라 생각하여 income이라 이름 붙이고
    # 띄워쓰기를 기준으로 값을 가지는 리스트로 바인딩 해 주었습니다.

    average = sum(income)/people
    # income을 sum 함수를 통해 더한 값을 사람수로 나누어 평균을 구해주었습니다.
    count = 0

    for each in income:
        if each <= average:
            count += 1
    # count를 0으로 잡고 income 리스트를 순회하며 평균값 이하의 수입을 거두는 사람이나오면 count에 값을 1씩 증가해 답을 구하였습니다.
    print(f'#{test_num} {count}')