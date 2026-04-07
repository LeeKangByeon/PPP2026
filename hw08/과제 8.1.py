def main():
    cal_dict = {
        "한라봉": 10, "딸기": 1
    }
    eat_dict = {
        "한라봉": 20, "딸기": 300
    }
    total_cal = 0
    for key, value in cal_dict.items():
        total_cal += cal_dict[key] * eat_dict[key]
    return total_cal

if __name__ == "__main__":
    print(main())

