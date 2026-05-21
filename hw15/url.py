import requests
import os

def read_weather(filename):

    tavgs = []
    rainfalls = []

    with open(filename) as f:
        lines = f.readlines()

        for line in lines[1:]:

            tokens = line.strip().split(",")

            tavg = float(tokens[4])
            rainfall = float(tokens[9])

            tavgs.append(tavg)
            rainfalls.append(rainfall)

    return tavgs, rainfalls


def average_temp(tavgs):

    return sum(tavgs) / len(tavgs)

def rainfall(rainfalls):

    count = 0

    for rain in rainfalls:
        if rain >= 5:
            count += 1

    return count


def total_rainfall(rainfalls):

    return sum(rainfalls)


def main():
    url = "https://api.taegon.kr/stations/146/?sy=2023&ey=2023&format=csv"
    resp = requests.get(url)

    filename = "weather(146)_2022-2022.csv"

    if not os.path.exists(filename):
        with open(filename, "w") as fout:
            fout.write(resp.text)


    tavgs, rainfalls = read_weather(filename)

    avg_temp = average_temp(tavgs)
    rain_day = rainfall(rainfalls)
    total_rain = total_rainfall(rainfalls)

    with open("result.txt", "w") as fout:

        fout.write(f"연 평균 기온: {avg_temp:.1f}℃\n")
        fout.write(f"5mm 이상 강우일수: {rain_day:.1f}일\n")
        fout.write(f"총 강우량: {total_rain:.1f}mm\n")

if __name__ == "__main__":
    main()