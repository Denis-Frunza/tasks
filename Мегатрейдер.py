def calculate_income_per_lot(N, day, price, qty):
    """
    Вычисляет общий доход от лота на день N + 30.
    """
    price_per_lot = price * qty * 10
    days_owned = (N + 30) - day
    coupon_income = qty * days_owned
    nominal_income = qty * 1000
    total_lot_income = coupon_income + nominal_income - price_per_lot
    return total_lot_income, price_per_lot

def calculate_max_income(N, M, budget, lots):
    total_income = 0
    selected_lots = []

    max_heap = []
    for day, name, price, qty in lots:
        total_lot_income, price_per_lot = calculate_income_per_lot(N, day, price, qty)
        heapq.heappush(max_heap, (-total_lot_income, price_per_lot, day, name, price, qty))

    while max_heap and budget > 0:
        lot_income, lot_price, day, name, price, qty = heapq.heappop(max_heap)
        lot_income = -lot_income
        if budget >= lot_price:
            budget -= lot_price
            total_income += lot_income
            selected_lots.append((day, name, price, qty))


    print(int(total_income))
    for day, name, price, qty in selected_lots:
        print(f"{day} {name} {price:.1f} {qty}")

if __name__ == "__main__":
    N, M, S = 2, 2, 8000
    lots = [
        (1, "alfa-05", 100.2, 2),
        (2, "alfa-05", 101.5, 5),
        (2, "gazprom-07", 100.0, 2)
    ]
    calculate_max_income(N, M, S, lots)

Временая сложность: O(M⋅Nlog(M⋅N))
Пространственная сложность: O(M⋅N)

Подход эффективен для больших данных так как жадный подход и heap выбор лотов с максимальной доходность.

Субъективная сложность:

8/10 задача требует эффективно находит лоты с максимальной доходностью
