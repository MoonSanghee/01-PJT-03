import sys

sys.stdin = open("_직사각형길이찾기.txt")

# 리스트에 입력받은 세 값을 넣고 if문을 통해 2값이 같은 경우와 세 값이 같은 경우를 비교하여
# 주려고했으나 시간 초과가 나와서 딕셔너리에 값을 넣고 입값이 홀수로 나오는 변을 찾아 출력해주는 방법으로 답을 구하였습니다.

test_case = int(1, input() + 1)

for test_num in range(test_case):
    each_line = list(map(int, input().split()))
    # 각 변을 리스트로 저장하였습니다.
    numbers = dict()
    for line in each_line:
        if line in numbers:
            numbers[line] += 1
        else:
            numbers[line] = 1
    # 입력값이 있으면 1번 더해주고 없으면 밸류값을 1로 설정하여 딕셔너리를 만들어 주었습니다.

    for i in numbers:
        if numbers[i] % 2 == 1:
            print(f'#{test_num} {i}')
        # 직사각형이 없는 경우가 없으므로 입력된 횟수가 홀수인 경우를 찾아 출력함으로써 답을 구하였습니다.