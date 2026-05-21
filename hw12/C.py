def two_rainfall(filename, year):

    total_rain = 0

    with open(filename) as f:
        lines = f.readlines()

        for line in lines[1:]:

            tokens = line.split(",")

            y = float(tokens[0])
            rain = float(tokens[9])

            # 원하는 연도이면
            if y == year:
                total_rain += rain

    return total_rain


def main():

    filename = "weather(146)_2001-2022.csv"

    rain_2021 = two_rainfall(filename, 2021)
    rain_2022 = two_rainfall(filename, 2022)

    print(f"2021년 총 강수량은: {rain_2021:.1f}mm입니다")
    print(f"2022년 총 강수량은: {rain_2022:.1f}mm입니다")


if __name__ == "__main__":
    main()