def calculate_percentages(N, shares):
    total_sum = sum(shares)

    for share in shares:
        percentage = share / total_sum
        print(f"{percentage:.3f}")

if __name__ == "__main__":
    N = 4
    shares = [1.5, 3, 6, 1.5]
    calculate_percentages(N, shares)

Временная сложность: O(N)
Пространственная сложность O(1)
На практике 𝑁=10^7(10000000)  до 5 секунд
Субъективная сложность: 2/10 .
