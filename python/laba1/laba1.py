import math
print('Сегмент окружности')
Yes = ''
while Yes == '':
    r = float(input('Введите радиус:>'))
    alfa = float(input('Введите угол:>'))
    l = math.pi * r * (alfa / 180)
    h = r * (1 - math.cos(alfa / 2))
    a = 2 * r * math.sin(l / 2 * r)

    p = l + a
    s = (r*(l-a) + a * h) / 2
    print('Периметр =', round(p, 3))
    print('Площадь =', round(s, 3))
    print('Область =', round(a, 3), "x", round(h, 3))
    Yes = input('[Enter]-Повторить ввод').strip()