cal_dict = {
    "한라봉": 10, "딸기": 1
    }
eat_dict = {
    "한라봉": 20, "딸기": 300
    }

total_cal = 0
for key, value in cal_dict.items():
    print(key, value)
    total_cal += cal_dict[key] * eat_dict[key]
    print(total_cal)