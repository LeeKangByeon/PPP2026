def read_weather(filename):

    tavgs = []
    rainfalls = []

    with open(filename) as f:
        lines = f.readlines()

        # 첫 줄(제목행)은 제외
        for line in lines[1:]:

            tokens = line.strip().split(",")

            # CSV에서 필요한 값 가져오기
            tavg = float(tokens[4])
            rainfall = float(tokens[9])

            tavgs.append(tavg)
            rainfalls.append(rainfall)

    return tavgs, rainfalls


def average_temperature(tavgs):

    return sum(tavgs) / len(tavgs)


def rainy_days(rainfalls):

    count = 0

    for rain in rainfalls:
        if rain >= 5:
            count += 1

    return count


def total_rainfall(rainfalls):

    return sum(rainfalls)


def main():

    filename = "weather(146)_2022-2022.csv"

    tavgs, rainfalls = read_weather(filename)

    avg_temp = average_temperature(tavgs)
    rain_day = rainy_days(rainfalls)
    total_rain = total_rainfall(rainfalls)

    print(f"연 평균 기온: {avg_temp:.2f}℃")
    print(f"5mm 이상 강우일수: {rain_day}일")
    print(f"총 강우량: {total_rain:.1f}mm")


if __name__ == "__main__":
    main()