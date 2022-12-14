
from random import sample

# 컴퓨터가 3자리 숫자를 문제로 내도록.

# 1~9로만 사용
# 중복된 숫자 허용 X

cpu_numbers = sample(range(1, 10), 3)

print(cpu_numbers)

# 사람이 3자리 숫자를 입력 => 맞출때 까지 계속 입력

# 시도 횟수를 기록하기 위한 변수
try_count = 0

while True:
    # 숫자 3개를 저장할 공간
    user_numbers = list()

    # 3자리 숫자를 입력 하면 => 3칸의 목록으로 분리
    input_num = int( input('3자리 숫자를 입력 : ') )

    # 입력 했으니 시도횟수 증가
    try_count += 1

    # ex. 123 => [1,2,3] 으로 분리.
    # 3자리 정수가 들어왔다고 전제하자.

    # 제일 먼저 추가 : 100의자리
    # 그 다음 : 10의자리
    # 그 다음 : 1의자리

    user_numbers.append( input_num // 100 ) # 100의자리
    user_numbers.append( input_num // 10 % 10 ) # 10의 자리
    user_numbers.append( input_num % 10 ) # 1의 자리

    print(user_numbers)

    # ?S ?B인지 판단 => 힌트 제공

    s_count = 0
    b_count = 0

    # 문제 숫자 / 내 숫자 비교 => S/B 갯수 파악

    # 내 숫자를 바꾸는 for

    for i, user_num in enumerate(user_numbers):

        # 문제 숫자와 비교하는 for
        for j, cpu_num in enumerate(cpu_numbers):

            # 같은 숫자여야, S/B이건 판단.
            if user_num == cpu_num:
                # 숫자가 같다면, 위치도 같은가?
                if i == j:
                    # 같다 : S 발견
                    s_count += 1
                else:
                    # 다르다 : 위치는 다르지만 숫자는 같다 : B 발견
                    b_count += 1

    # S/B 판정 끝나면 출력
    print(f'{s_count}S {b_count}B 입니다.')

    # 문제 1. 3S가 되었다면? => 정답 맞춤! (축하 문구) => 게임 종료

    if s_count == 3:
        print('축하합니다! 정답입니다!')

        # 시도횟수도 출력
        print(f'{try_count}회만에 맞췄습니다!')

        break

    # 문제 2. 종료 전에, 몇번의 시도만에 맞췄는지. 7회만에 맞췄습니다.
