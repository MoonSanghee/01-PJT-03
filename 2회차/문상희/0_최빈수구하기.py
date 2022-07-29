import sys

sys.stdin = open("_최빈수구하기.txt")

# 가장 많이 나온 수를 구하고 그 값이 여렇이면 큰 수를 구하라고하여서 각 숫자를 몇 개씩 가지는지
# 딕셔너리 형태로 가장 많은 수가 여렇이면 리스트에 모아 가장 큰 값을 출력하도록 접근했습니다.

test_case = int(input())


for i in range(1, test_case + 1):
    tes_num = int(input())
    # 출력되지 않지만 테스트 회차가 입력되므로 input값을 받는 코드를 작성해 주었습니다.
    all_point = list(map(int, input().split()))

    points = dict()

    for point in all_point:
        if point in points:
            points[point] += 1
        else:
            points[point] = 1
    # 입력값이 딕셔너리에 없으면 밸류값을 1로 주고 있으면 1씩 추가해 주었습니다.
    count = 0
    # 점수의 갯수가 가장 많은 수인지 비교해줄 변수를 설정해 주었습니다.
    for point in points:
        if points[point] > count:
            most_nums = []
            most_nums.append(point)
            count = points[point]
            # 점수가 갱신 되었으면 리스트를 비우고 빈 리스트에 갱신시킬때 키값을 넣어주었습니다.
        elif points[point] == count:
            most_nums.append(point)
            # 가장 많은 점수와 같은 경우 점수가 더 큰지 비교하기 위해 만들어준 리스트에 값을 추가해 주었습니다.

    print(f'#{i} {max(most_nums)}')
            # 리스트에서 가장 큰 값을 출력해 주었습니다.