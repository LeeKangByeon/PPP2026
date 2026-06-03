import matplotlib.pyplot as plt


def read_weather_col(weather_filename, col_idx=9, conv_fn=float):
    dataset = []

    with open(weather_filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(conv_fn(tokens[col_idx]))

    return dataset


def main():
    jeonju_filename = "weather(146)_1980-2024 (2).csv"
    suwon_filename = "weather(119)_1980-2024 (1).csv"

    # 전주 데이터
    jeonju_years = read_weather_col(jeonju_filename, 0, int)
    jeonju_months = read_weather_col(jeonju_filename, 1, int)
    jeonju_days = read_weather_col(jeonju_filename, 2, int)
    jeonju_tavg = read_weather_col(jeonju_filename, 4, float)
    jeonju_rainfalls = read_weather_col(jeonju_filename, 9, float)

    # 수원 데이터
    suwon_years = read_weather_col(suwon_filename, 0, int)
    suwon_tavg = read_weather_col(suwon_filename, 4, float)

    years = list(range(1980, 2025))

    # -------------------------------------------------
    # 5. 1980~2024년 전주시와 수원시의 연평균 기온
    # -------------------------------------------------

    jeonju_yearly_tavg = []
    suwon_yearly_tavg = []

    for year in years:
        jeonju_selected = []
        suwon_selected = []

        for i in range(len(jeonju_years)):
            if jeonju_years[i] == year:
                jeonju_selected.append(jeonju_tavg[i])

        for i in range(len(suwon_years)):
            if suwon_years[i] == year:
                suwon_selected.append(suwon_tavg[i])

        jeonju_avg = sum(jeonju_selected) / len(jeonju_selected)
        suwon_avg = sum(suwon_selected) / len(suwon_selected)

        jeonju_yearly_tavg.append(jeonju_avg)
        suwon_yearly_tavg.append(suwon_avg)

    plt.figure()
    plt.plot(years, jeonju_yearly_tavg, label="Jeonju")
    plt.plot(years, suwon_yearly_tavg, label="Suwon")
    plt.title("Annual Average Temperature")
    plt.xlabel("Year")
    plt.ylabel("Temperature (C)")
    plt.legend()
    plt.grid()
    plt.show()

    # -------------------------------------------------
    # 6. 1980~2024년 전주시의 연간 강수량
    # -------------------------------------------------

    jeonju_yearly_rainfall = []

    for year in years:
        total_rainfall = 0

        for i in range(len(jeonju_years)):
            if jeonju_years[i] == year:
                total_rainfall += jeonju_rainfalls[i]

        jeonju_yearly_rainfall.append(total_rainfall)

    plt.figure()
    plt.bar(years, jeonju_yearly_rainfall)
    plt.title("Annual Rainfall in Jeonju")
    plt.xlabel("Year")
    plt.ylabel("Rainfall (mm)")
    plt.show()

    # -------------------------------------------------
    # 7. 생일인 8월 27일의 전주시 평균기온 변화
    # -------------------------------------------------

    birthday_month = 8
    birthday_day = 27
    birth_year = 2004

    birthday_years = []
    birthday_tavg = []

    for i in range(len(jeonju_years)):
        if jeonju_months[i] == birthday_month:
            if jeonju_days[i] == birthday_day:
                birthday_years.append(jeonju_years[i])
                birthday_tavg.append(jeonju_tavg[i])

    plt.figure()
    plt.plot(birthday_years, birthday_tavg, marker="o")
    plt.title("Temperature on August 27 in Jeonju")
    plt.xlabel("Year")
    plt.ylabel("Temperature (C)")
    plt.grid()
    plt.show()

    # -------------------------------------------------
    # 7-1. 1980~2014년 사이에서 생일 기온 순위 구하기
    # -------------------------------------------------

    selected_years = []
    selected_tavg = []

    for i in range(len(birthday_years)):
        if 1980 <= birthday_years[i] <= 2014:
            selected_years.append(birthday_years[i])
            selected_tavg.append(birthday_tavg[i])

    birth_year_temperature = 0

    for i in range(len(selected_years)):
        if selected_years[i] == birth_year:
            birth_year_temperature = selected_tavg[i]

    sorted_tavg = sorted(selected_tavg, reverse=True)
    ranking = sorted_tavg.index(birth_year_temperature) + 1

    highest_temperature = max(selected_tavg)
    lowest_temperature = min(selected_tavg)

    highest_index = selected_tavg.index(highest_temperature)
    lowest_index = selected_tavg.index(lowest_temperature)

    highest_year = selected_years[highest_index]
    lowest_year = selected_years[lowest_index]

    print(f"2004년 8월 27일 전주시 평균기온은 {birth_year_temperature:.1f}도입니다.")
    print(f"1980~2014년 사이에서 {ranking}번째로 기온이 높았습니다.")
    print(f"가장 기온이 높았던 해는 {highest_year}년입니다.")
    print(f"가장 기온이 낮았던 해는 {lowest_year}년입니다.")


if __name__ == "__main__":
    main()