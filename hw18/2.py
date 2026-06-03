def caesar_encode(text, shift=3):
    result = ""

    for alphabet in text:
        if 'A' <= alphabet <= 'Z':
            new_code = (ord(alphabet) - ord('A') + shift) % 26 + ord('A')
            result += chr(new_code)

        elif 'a' <= alphabet <= 'z':
            new_code = (ord(alphabet) - ord('a') + shift) % 26 + ord('a')
            result += chr(new_code)

        else:
            result += alphabet

    return result

def caesar_decode(text, shift=3):
    result = ""

    for alphabet in text:
        if 'A' <= alphabet <= 'Z':
            new_code = (ord(alphabet) - ord('A') - shift) % 26 + ord('A')
            result += chr(new_code)

        elif 'a' <= alphabet <= 'z':
            new_code = (ord(alphabet) - ord('a') - shift) % 26 + ord('a')
            result += chr(new_code)

        else:
            result += alphabet

    return result



def main():

    encode_text = input("카이사르 암호화:")
    decode_text = input("카이사르 암호 해석:")

    encode_result = caesar_encode(encode_text)
    decode_result = caesar_decode(decode_text)

    print(encode_result)
    print(decode_result)


if __name__ == '__main__':
    main()