def top_down(n) -> int:
    number = [0] * 100

    def fibo(n) -> int:
        if n == 1 or n == 2:
            return 1

        if number[n] != 0:
            return number[n]

        number[n] = fibo(n - 1) + fibo(n - 2)
        return number[n]

    return fibo(n)


def bottom_up(n) -> int:
    number = [0] * 100

    number[1] = 1
    number[2] = 1

    for i in range(3, n + 1):
        number[i] = number[i - 1] + number[i - 2]

    return number[n]


n = int(input())
print(top_down(n))
print(bottom_up(n))
