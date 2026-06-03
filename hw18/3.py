import csv
import random


K_list = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ',
    'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
    'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ',
    'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]


def read_movie_col(movie_filename, col_idx=0, conv_fn=str):
    dataset = []

    with open(movie_filename, "r", encoding="utf-8-sig") as f:
        lines = csv.reader(f)

        next(lines)

        for tokens in lines:
            dataset.append(conv_fn(tokens[col_idx]))

    return dataset


def get_initial(char):
    if '가' <= char <= '힣':
        index = (ord(char) - ord('가')) // 588
        return K_list[index]

    return char



def make_initial_quiz(movie):
    result = ""

    for char in movie:
        result += get_initial(char)

    return result


def main():
    movie_filename = "천만_관객_영화_목록.csv"

    movies = read_movie_col(movie_filename, 0)

    selected_movie = random.choice(movies)
    quiz = make_initial_quiz(selected_movie)

    print("다음 초성에 해당하는 천만 관객 영화는 무엇일까요?")
    print(quiz)

    answer = input("정답: ")

    if answer == selected_movie:
        print("정답입니다")
    else:
        print("틀렸습니다")
        print("정답은", selected_movie, "입니다.")


if __name__ == "__main__":
    main()


