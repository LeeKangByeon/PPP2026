import tkinter as tk
from tkinter import simpledialog
import requests


Root = tk.Tk()
Root.withdraw()




# 전주의 현재 온도 가져오기
def get_temp():

    url = "https://api.open-meteo.com/v1/forecast?latitude=35.8242&longitude=127.1480&current=temperature_2m"

    weather = requests.get(url).json()

    temperature = weather["current"]["temperature_2m"]

    return temperature



# CSV 파일에서 작물별 온도 기준 가져오기
def get_crop(crop):

    with open("작물.csv", "r", encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:

            tokens = line.strip().split(",")

            crop_name = tokens[0]
            min_limit_temp = float(tokens[1])

            proper_temp = tokens[2].split("~")
            min_temp = float(proper_temp[0])
            max_temp = float(proper_temp[1])

            max_limit_temp = float(tokens[3])

            if crop == crop_name:
                return min_limit_temp, min_temp, max_temp, max_limit_temp

    return None



# 온도가 적절한지 확인하기
def check_temperature(temperature, min_limit_temp, min_temp, max_temp, max_limit_temp):

    danger_range = 2

    if temperature <= min_limit_temp + danger_range:
        return "위험한 수준의 온도입니다"

    elif temperature >= max_limit_temp - danger_range:
        return "위험한 수준의 온도입니다"

    elif min_temp <= temperature <= max_temp:
        return "적절한 온도입니다"

    else:
        return "주의해야 할 온도입니다"



# 작물 입력창 띄우기
def gui_input(text):

    return simpledialog.askstring(
        title="작물 선택",
        prompt=text
    )




def main():

    crop = gui_input(
        "작물을 입력해주세요\n"
        "토마토, 가지, 고추, 오이, 수박, 온실멜론, 참외, 호박, 시금치, 무, 배추, 셀러리, 쑥갓, 결구상추, 딸기"
    )

    if crop is None:
        print("창을 닫았습니다")

    elif crop == "":
        print("작물이 입력되지 않았습니다")

    else:
        standard = get_crop(crop)

        if standard is None:
            print("토마토, 가지, 고추, 오이, 수박, 온실멜론, 참외, 호박, 시금치, 무, 배추, 셀러리, 쑥갓, 결구상추, 딸기 중에서 입력해주세요")

        else:
            temperature = get_temp()

            min_limit_temp = standard[0]
            min_temp = standard[1]
            max_temp = standard[2]
            max_limit_temp = standard[3]

            temp_result = check_temperature(
                temperature,
                min_limit_temp,
                min_temp,
                max_temp,
                max_limit_temp
            )


            print("[입력 작물]")
            print(crop)
            print("\n")

            print("[전주의 현재 외부 날씨]")
            print(f"온도: {temperature}℃")
            print("\n")

            print(f"[{crop}의 온도]")
            print(f"최저한계온도: {min_limit_temp}℃")
            print(f"생육적온: {min_temp}~{max_temp}℃")
            print(f"최고한계온도: {max_limit_temp}℃")
            print("\n")

            print("[결론]")
            print(temp_result)


if __name__ == "__main__":
    main()