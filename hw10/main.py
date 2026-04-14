def average_list(nums):
    return sum(nums) / len(nums)

def read_text(filename):
    with open(filename) as f:
        text = f.readline()
        return text

def text2list(text):
    nums = [int(x) for x in text.split(",")]
    return nums

def main():
    input_text = read_text("number1.txt")
    nums = text2list(input_text)
    print("주어진 리스트는:", nums)
    print("총 숫자의 개수는:", len(nums))
    print(average_list(nums))
    print(max(nums))
    print(min(nums))
    print(nums[2])

if __name__ == "__main__":
    main()