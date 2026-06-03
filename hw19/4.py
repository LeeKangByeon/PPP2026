def main():
    word = "apple"
    answer = ["_"] * len(word)
    k = 0

    while "_" in answer:
        print("현재 상태:", " ".join(answer))

        guess = input("알파벳 한 글자를 입력하세요: ")

        if guess in word:
            print("Correct!")

            for i in range(len(word)):
                if word[i] == guess:
                    answer[i] = guess
        else:
            k += 1
            print(f"Wrong!  틀린 횟수{k}")

            if k == 3:
                print("you are die")
                return





    print("정답입니다:", word)


if __name__ == "__main__":
    main()
