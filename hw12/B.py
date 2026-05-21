def summer_rainfall(filename):

    total_rain = 0

    with open(filename) as f:
        lines = f.readlines()

        for line in lines[1:]:

            tokens = line.split(",")

            month = float(tokens[1])
            rain = float(tokens[9])

            if month in [6, 7, 8]:
                total_rain += rain

    return total_rain


def main():

    filename = "weather(146)_2022-2022.csv"

    result = summer_rainfall(filename)

    print(f"6,7,8월 총 강수량은: {result:.1f}mm입니다" )


if __name__ == "__main__":
    main()