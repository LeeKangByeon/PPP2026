import math
x = int(input("x을 적으시오"))
y = int(input("y을 적으시오"))
if x > 0 and y > 0:
    print("입력한 좌표는 1사분면입니다")
elif x < 0 and y > 0:
    print("입력한 좌표는 2사분면입니다")
elif x < 0 and y < 0:
    print("입력한 좌표는 3사분면입니다")
elif x > 0 and y < 0:
    print("입력한 좌표는 4사분면입니다")




