import random

def lotto():
    numbers = random.sample(range(1, 46), 6)
    return numbers




def main():
    result = lotto()
    print(f"회차 1227  당첨번호  {result}입니다")


if __name__ == "__main__":
    main()