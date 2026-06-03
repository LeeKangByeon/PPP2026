def read_weather_col(weather_filename, col_idx=9, conv_fn=float):
    dataset = []

    with open(weather_filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(conv_fn(tokens[col_idx]))

    return dataset


def sumifs(values, years, selected_year):
    total_value = 0

    for i in range(len(values)):
        if years[i] == selected_year:
            total_value += values[i]

    return total_value


def main():
    jeonju_filename = "weather(146)_1980-2024 (2).csv"
    suwon_filename = "weather(119)_1980-2024 (1).csv"

    # 전주 데이터
    jeonju_years = read_weather_col(jeonju_filename, 0, int)
    jeonju_tmax = read_weather_col(jeonju_filename, 3, float)
    jeonju_tmin = read_weather_col(jeonju_filename, 5, float)
    jeonju_rainfalls = read_weather_col(jeonju_filename, 9, float)

    # 수원 데이터
    suwon_years = read_weather_col(suwon_filename, 0, int)
    suwon_rainfalls = read_weather_col(suwon_filename, 9, float)

    # 1. 전주시의 2012년 연 강수량
    rainfall_2012 = sumifs(jeonju_rainfalls, jeonju_years, 2012)

    # 2. 전주시의 2024년 최대기온
    tmax_2024 = []

    for i in range(len(jeonju_years)):
        if jeonju_years[i] == 2024:
            tmax_2024.append(jeonju_tmax[i])

    max_tmax_2024 = max(tmax_2024)

    # 3. 전주시의 2020년 최대 일교차
    temp_range_2020 = []

    for i in range(len(jeonju_years)):
        if jeonju_years[i] == 2020:
            temp_range = jeonju_tmax[i] - jeonju_tmin[i]
            temp_range_2020.append(temp_range)

    max_temp_range_2020 = max(temp_range_2020)

    # 4. 수원시와 전주시의 2019년 총강수량 차이
    jeonju_rainfall_2019 = sumifs(jeonju_rainfalls, jeonju_years, 2019)
    suwon_rainfall_2019 = sumifs(suwon_rainfalls, suwon_years, 2019)

    rainfall_difference = abs(jeonju_rainfall_2019 - suwon_rainfall_2019)

    print(f"1. 전주시의 2012년 연 강수량은 {rainfall_2012:.1f}mm입니다.")
    print(f"2. 전주시의 2024년 최대기온은 {max_tmax_2024:.1f}도입니다.")
    print(f"3. 전주시의 2020년 최대 일교차는 {max_temp_range_2020:.1f}도입니다.")
    print(f"4. 수원시와 전주시의 2019년 총강수량 차이는 {rainfall_difference:.1f}mm입니다.")


if __name__ == "__main__":
    main()