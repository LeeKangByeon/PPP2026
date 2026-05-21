def str2int(text):

    try:
        number = int(text)
        return number

    except:
        return None


def main():

    v = []

    while True:

        x = input("X=? ")

        number = str2int(x)

        if number == -1:
            break

        if number is not None:

            if number > 0:
                v.append(number)

    c = len(v)

    avg = sum(v) / c

    print(f"입력된 값은 {v} 입니다. 총 {c}개의 자연수가 입력되었고, 평균은 {avg:.1f}입니다 ")


if __name__ == "__main__":
    main()