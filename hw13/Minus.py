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



def get_max_diff(dates, tmax, tmin):
    max_diff = -999
    max_diff_date = None

    for i in range(len(dates)):
        diff = tmax[i] - tmin[i]

        if diff > max_diff:
            max_diff = diff
            max_diff_date = dates[i]

    return max_diff_date, max_diff




def main():
    weather_filename = "weather(146)_2022-2022.csv"
    dates = read_dates(weather_filename)
    tmax = read_weather_col(weather_filename, 3)
    tmin = read_weather_col(weather_filename, 5)
    date, temp_diff = get_max_diff(dates, tmax, tmin)
    print(f"일교차가 가장 큰 날: {date}")
    print(f"일교차가 가장 큰 날의 일교차는 {temp_diff}c")

if __name__ == "__main__":
    main()