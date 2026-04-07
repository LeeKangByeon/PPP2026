def main():
    y = int(input("연도를 입력하세요, 윤년인지 아닌지를 알려드립니다:"))
    if y % 4 == 0 and y % 100 != 0:
        print("true")
    else :
        print("false")
if __name__ == "__main__":
    main()