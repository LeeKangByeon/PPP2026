def read_dates(weather_filename):
    dates = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            date = [int(tokens[0]), int(tokens[1]), int(tokens[2])]
            dates.append(date)

    return dates

def read_weather_col(weather_filename, col_idx):
    values = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            value = float(tokens[col_idx])
            values.append(value)

    return values



def gdd_season(dates, tavg):
    gdd_value = 0
    for i in range(len(dates)):
        date = dates[i]
        t = tavg[i]
        if date[1] in [5,6,7,8,9]:
            if t > 5:
                gdd_value += (t - 5)

    return gdd_value



def main():
    weather_filename = "weather(146)_2022-2022.csv"
    dates = read_dates(weather_filename)
    tavg = read_weather_col(weather_filename, 9)

    gdd_value = gdd_season(dates, tavg)
    print(f"GDD는 {gdd_value}입니다")

if __name__ == "__main__":
    main()