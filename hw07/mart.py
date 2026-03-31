mart = {"우유": 2800, "계란": 300, "빵": 1200, "물": 1700}
total_cost = 0
for key, value in mart.items():
    total_cost += mart[key]
print(f"총 구매 금액은 {total_cost}원 입니다")