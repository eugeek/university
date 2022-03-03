# Функция вычисления факториала N!
def Factorial(n):
    result = 1.0
    k = 1
    if n > 1:
        k = 2
    while k <= n:
        result *= k
        k += 1
    return result


# Функция вычисления целой степени X^N
def Power(x, n):
    divide = False
    result = 1.0
    if n < 0:
        divide = True
        n = -n
    k = 1
    while k <= n:
        result *= x
        k += 1
    if divide == True:
        result = (1 / result)
    return result


def Calculate(m):
    i = 1
    z = -1
    result = 0.0
    while i <= m:
        result = result + Factorial(m - i) / Power(m - i + 1, 2) * z
        z = z * (-1)
        i = i + 1
    return result


# Главная функция реализует интерфейс с пользователем
def main():
    Yes = 'да'
    while Yes == 'да' or Yes == 'yes':
        value = int(input('Введите число [1..12]:>'))
        if value < 1 or value > 12:
            print(' - некорректное значение')
        else:
            result = Calculate(value)
            print('Результат (', value, ') = ', result)
        print()
        Yes = input('Повторить ввод [да|yes]:>')
        Yes = Yes.lower()
        print()


if __name__ == '__main__':
    main()