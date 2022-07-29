import sys

sys.stdin = open("_암호문1.txt")

for test_num in range(1, 11):
    print(f'#{test_num}', end = ' ')
    first_scy = int(input())
    firstscy_list = list(map(str, input().split()))
    command_cnt = int(input())
    each_command = list(map(str, input().split()))
    # 명령어가 I를 기준으로 나뉘어 입력되어 문자열이 포함된 값을 주므로 입력값을 문자열로
    # 받아 리스트로 저장해 주었습니다.
    
    new_list = firstscy_list
    for i in range(len(each_command)):
        if each_command[i - 1] == 'I':
            nlh = new_list[:int(each_command[i]):]
            nlt = new_list[int(each_command[i])::]
        if each_command[i] != 'I' and each_command[i - 1] != 'I' and each_command[i - 2] != 'I':
            nlh.append(each_command[i])
            new_list = nlh + nlt
    # 명령어에서 I가 나오고 다음 자리에 넣어줄 위치 그 다음 자리에 갯수가 나오므로 
    # I가 나온 다음 자리 값을 기준으로 원본 암호문을 쪼개고 그 앞쪽 리스트에
    # I가 나온 자리(1)부터 다음 I(2)가 나오기 전까지 I가 나온자리,그(1) 다음 자리와 (1)의 다다음자리를 제외한 값들을
    # 차례대로 I를 기준으로 짜른 앞쪽리스트에 추가해줍니다.
    # 그리고 I 다음으로 쪼갤 기준이 되는 값이 나오기 전까지 추가한 앞값과 쪼갠 뒷값을 합하여 새로운 리스트로 만들어줍니다.
    
    
    for i in range(10):
        print(new_list[i], end = ' ')
    # 리스트 형태가 아닌 각 자리 값만을 출력하므로 테스트 회차가 시작되기 전에 print(f'#{i}', end = ' ')를 통해
    # 테스트 회차를 입력해주고 범위를 10까지로 반복하며 마지막에 저장된 리스트의 9번자리까지의 값들을 한 칸 띄워 출력해주었습니다.
    print()
    #위에 반복을 마치고 끝을내면 회차가 끝나고 줄이 바뀌지 않으므로 리스트 속 값 반복을 마치고 리스트 밖에서 줄바꿈을 해 주었습니다.
