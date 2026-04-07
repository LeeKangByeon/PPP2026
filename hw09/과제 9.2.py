def main():
    n = int(input("n값을 입력하시오."))
    num = []
    for i in range(n+1):
        num.append(i)
    return num

if __name__ == "__main__":
    print(main())