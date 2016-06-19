# coding: utf-8

from random import randint
import sys

SHIPS 	  = [1,1,1,1,2,2,2,3,3,4]
SEA_CHAR  = '~'
SHIP_CHAR = 'x'
SEAMAP    = []
N 	   	  = 10
ALPHABLET = 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

# функция для нахождения соседней точки корабля в окрестности текущей точки
# возвращает координаты первой соседней точки или саму точку в случае отсутсвия соседа
def get_neibor(x, y, matrix):
	
	global N

	if x - 1 >= 0:
		if matrix[x - 1][y] > 0:
			return x - 1, y
	if x + 1 < N:
		if matrix[x + 1][y] > 0:
			return x + 1, y
	if y - 1 >= 0:
		if matrix[x][y - 1] > 0:
			return x, y - 1
	if y + 1 < N:
		if matrix[x][y + 1] > 0:
			return x, y + 1

	if x + 1 < N and y + 1 < N:
		if matrix[x + 1][y + 1] > 0:
			return x + 1, y + 1	
	if x - 1 >= 0 and y - 1 >= 0:
		if matrix[x - 1][y - 1] > 0:
			return x - 1, y - 1
	if x + 1 < N and y - 1 >= 0:
		if matrix[x + 1][y - 1] > 0:
			return x + 1, y - 1
	if x - 1 >= 0 and y + 1 < N:
		if matrix[x - 1][y + 1] > 0:
			return x - 1, y + 1

	return x, y


# проверка на длину карты
if N > len(ALPHABLET):
	N = len(ALPHABLET)

if __name__ == '__main__':
	# генерируем пустую карту NxN
	for y in range(N):
		SEAMAP.append([0 for x in range(N)])

	# пробегаемся в=по всем кораблям
	for ship_len in SHIPS:
		while False:
			# создаем координаты для случайной точки
			x = randint(0, N - 1)
			y = randint(0, N - 1)
			
			point = SEAMAP[x][y]

			# проверяем, есть ли в текущей точке корабль (0 - корабля нет, 1 - корабль есть)
			# если корабля нет, то продолжаем цикл заново
			if point > 0:
				continue

			# иначе находим ближайшего соседа к текущей точке
			nx, ny = get_neibor(x, y, SEAMAP)
			
			# если в окрестности нашей точки не найдено ни одного соседнего корабля...
			if nx == x and ny == y:
				# то выбираем ориентацию нашего корабля (0 - горизонтальная, 1 - вертикальная)
				d = randint(0, 1)
				
				# @todo написать функцию построения корабля

				# строим вертикальный корабль...
				if d > 0:
					# вариант вверх
					for my in range(y - ship_len, y):
						pass
					# вариант вниз
					for my in range(y, y + ship_len):
						pass
				# строим горизонтльный корабль...
				else:
					# вариант налево
					for mx in range(x - ship_len, x):
						pass
					# вариант направо
					for mx in range(x, x + ship_len):
						pass


	# рисуем карту в консоль
	for y in range(N):
		if y == 0:
			sys.stdout.write(' ' * 4)
			for x in range(N):
				hn = ALPHABLET[x : x + 1]
				sys.stdout.write(' ' + hn + ' ' * 2)
			sys.stdout.write('\n')		

		sys.stdout.write(' ' * 3 + '+')
		sys.stdout.write(('-' * 3 + '+') * N)
		sys.stdout.write('\n')

		vn = y + 1
		if vn < 10:
			vn = '0' + str(vn)
		else:
			vn = str(vn)

		sys.stdout.write(vn + ' | ')

		for x in range(N):
			if SEAMAP[x][y] > 0:
				sys.stdout.write(SHIP_CHAR)
			else:
				sys.stdout.write(SEA_CHAR)
			sys.stdout.write(' | ')
		sys.stdout.write('\n')

	sys.stdout.write(' ' * 3 + '+')
	sys.stdout.write(('-' * 3 + '+') * N)
	sys.stdout.write('\n')