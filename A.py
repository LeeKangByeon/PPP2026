def longest_rain_days(lines):

    max_day = 0
    day = 0

    for line in lines:

        tokens = line.split(",")

        rain = float(tokens[13])

        # 비가 오면
        if rain > 0:

            day = day + 1

            # 최대값 비교
            if day > max_day:
                max_day = day

        # 비가 안 오면
        else:
            day = 0

    return max_day



def max_rain_event(lines):

    max_rain = 0
    total_rain = 0

    for line in lines:

        tokens = line.split(",")

        rain = float(tokens[13])

        # 비가 오면 계속 더하기
        if rain > 0:
            total_rain = total_rain + rain

        # 비가 안 오면 비교
        else:

            if total_rain > max_rain:
                max_rain = total_rain

            total_rain = 0

    return max_rain



def hottest_top3(lines):

    temps = []

    for line in lines:

        tokens = line.split(",")

        temp = float(tokens[4])

        temps.append(temp)

    temps.sort()

    print("가장 더운 날 TOP 3")
    print(temps[-1])
    print(temps[-2])
    print(temps[-3])



def main():

    # 파일 열기
    f = open("weather(146)_2022-2022.csv")

    # 한 줄씩 읽기
    lines = f.readlines()

    # 제목줄 제거
    lines = lines[1:]


    # 함수 실행
    rain_days = longest_rain_days(lines)

    max_rain = max_rain_event(lines)


    # 결과 출력
    print("최장 연속 강우일수:", rain_days)

    print("최대 강우 이벤트 강수량:", max_rain)

    hottest_top3(lines)


    # 파일 닫기
    f.close()


if __name__ == "__main__":
    main()