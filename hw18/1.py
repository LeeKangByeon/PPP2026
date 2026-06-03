def toggle_ch(alphabet):
    if ord(alphabet) >= 65 and ord(alphabet) <= 90:
        return chr(ord(alphabet) + 32)
    elif ord(alphabet) >= 97 and ord(alphabet) <= 122:
        return chr(ord(alphabet) - 32)
    else:
        return alphabet


def toggle_text(text):
    result = ""
    for c in text:
        result += toggle_ch(c)
    return result


def main():
    text = input("문자열을 입력하시오:")
    result = toggle_text(text)
    print(result)


if __name__ == '__main__':
    main()