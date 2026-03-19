print("1번은: C -> F로 변환 해드립니다")
print("2번은: F -> C로 변환 해드립니다")
print("3번은: 피트 -> cm로 변환 해드립니다")
print("4번은: cm를 -> 피트로 변환 해드립니다")
choice = int(input("번호를 입력하세요:"))
if choice == 1:
    temp_c = int(input("섭씨 온도를 입력해주세요"))
    temp_f = temp_c * 1.8 + 32
    print(f"화씨온도는: {temp_f:.1f}")
elif choice == 2:
    temp_f = int(input("화씨 온도를 입력해주세요"))
    temp_c = (temp_f - 32) *5/9
    print(f"섭씨온도는: {temp_c:.1f}")
elif choice == 3:
    F = int(input("피트 값을 입력해주세요"))
    C = F * 30.48
    print(f"cm는: {C:.1f}")
elif choice == 4:
    C = int(input("cm 값을 입력해주세요"))
    F = C / 30.48
    print(f"피트는: {F:.1f}")

