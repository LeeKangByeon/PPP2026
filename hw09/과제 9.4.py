def main():
    input_text = input("숫자 리스트를 입력하시오 ,로 구분:")
    nums = [int(x) for x in input_text.split(",")]
    average = sum(nums) / len(nums)
    return average
if __name__ == "__main__":
    print(main())