import math
W =  float(input("자신의 몸무게를 입력하시오"))
H = float(input("자신의 키를 입력하시오"))
BMI = W / H ** 2
print("당신의  BMI는:", BMI)
if 23 <= BMI < 24.9:
    print("당신은 비만 전단계입니다.")
elif 25 <= BMI < 29.9:
    print("당신은 1단계 비만입니다")
elif 30 <= BMI < 34.9:
    print("당신은 2단계 비만입니다")
elif BMI >= 35:
    print("당신은 3단계 비만입니다")
