import math

def Entry(message):
	value = ''
	while value == '':
		value = input(message).strip()
		try:
			value = float(value)
			break
		except ValueError:
			print('Ошибка: требуется ввести числовое значение')
			value = ''
	return value

def PrintXY(x, y):
	print('F(', round(x, 2), ') = ', round(y, 4), sep = '')

def main():
	print('Вычисление функции на интервале')
	Yes = 'да'
	while Yes == 'да':
		num = input('Выберите функцию [1:(exp(-x)-x)|2:(x+x^3-5)|3:(cos(2x)-x)]:>')
		if num == '1':
			f = lambda x: math.exp(-x) - x
		elif num == '2':
			f = lambda x: x**3 + x - 5
		elif num == '3':
			f = lambda x: math.cos(2 * x) - x
		else:
			print('Ошибка: неправильный номер функции')
			continue
		left = Entry('Введите левую границу интервала:>')
		right = Entry('Введите правую границу интервала:>')
		if left > right:
			left, right = right, left
		step = Entry('Введите шаг на интервале:>')
		if step < 0.000001 or step > (right - left)/3.0:
			print('Ошибка: некорректное значение шага')
			continue
		x_less = x_most = x = left
		y_less = y_most = y = f(left)
		PrintXY(x, y)
		x += step
		while x <= right:
			y = f(x)
			if y < y_less:
				y_less = y
				x_less = x
			if y > y_most:
				y_most = y
				x_most = x
			PrintXY(x, y)
			x += step
		print('Наименьшее', end = ': '); PrintXY(x_less, y_less)
		print('Наибольшее', end = ': '); PrintXY(x_most, y_most)
		Yes = input('Повторить расчёт [да]:>').strip().lower()
		print()
	print('Завершение вычислений')


if __name__ == '__main__':
	main()