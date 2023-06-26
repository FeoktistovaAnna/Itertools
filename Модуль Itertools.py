# Функции, фильтрующие данные

# dropwhile(функция-предикат, итерируемая последовательность) -
# возвращает итератор, который генерирует элементы из
# входного итерируемого объекта сразу после того, как
# для заданного условия будет получено ложное значение
from itertools import dropwhile

numbers = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
words = ['is', 'an', 'of', 'python', 'C#', 'beegeek', 'is']

new_numbers = list(dropwhile(lambda num: num <= 5, numbers))
#print(new_numbers)

#for word in dropwhile(lambda s: len(s) == 2, words):
    #print(word, end=' ')

''' Функция dropwhile() не выдаст никаких выходных данных до тех пор,
 пока функция-предикат не вернёт False, поэтому
 она может иметь долгое время запуска'''

''' Вместо лямбда-функции можно использовать обычную '''

#def should_drop(x):
    #print('Testing:', x)
    #return x < 1

#for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
    #print('Yielding: ', i)

# Функция dropwhile() эквивалентна коду:

def dropwhile(predicate, iterable):
    it = iter(iterable)
    for elem in it:
        if not predicate(elem):
            yield elem
            break
    for elem in it:
        yield elem

''' Функция takewhile() возвращает итератор, который 
 генерирует элементы из входной итерируемой последовательности, 
 пока для заданного условия не будет получено ложное значение
 По сути - действия противоположны dropwhile()'''

from itertools import takewhile

new_numbers = list(takewhile(lambda num: num <=5, numbers))
#print(new_numbers)

#for word in takewhile(lambda c: len(c) == 2, words):
    #print(word, end=' ')

# Определяем функцию-предикат

def should_take(x):
    print('Testing:', x)
    return x < 2

#for i in takewhile(should_take, [-1, 0, 1, 2, -2]):
    #print('Yielding:', i)

# Функция takewhile() эквивалентна следующему коду:

def takewhile(predicate, iterable):
    # iterable = iter(iterable) почему в дропвайл эта строка нужна, а тут нет?
    for elem in iterable:
        if predicate(elem):
            yield elem
        else:
            break

''' Функция filterfalse() возвращает итератор, который 
 генерирует элементы из входной итерируемой последовательности,
 для которых не выполняется функция-предикат. То есть эта
 функция противоположна функции filter()'''

from itertools import filterfalse

new_numbers = list(filterfalse(lambda num: num <=5, numbers))
#print(new_numbers)
#for word in filterfalse(lambda c: len(c) == 2, words):
#    print(word, end=' ')

# Если predicate=None, то фильтрующая функция равнозначна функции bool()

# Объявляю функцию-предикат
def check_items(x):
    print('Testing:', x)
    return x < 1

#for i in filterfalse(check_items, [-1, 0, 1, 2, -2]):
#    print('Yielding:', i)

# Функция  filterfalse() эквивалентна коду:
def filterfalse(predicate, iterable):
    if predicate is None:
        predicate = bool
    for i in iterable:
        if not predicate(i):
            yield i

''' Функция compress() принимает две итерируемые последовательности.
 Первая состоит из проверяемых значений,
 вторая из True и False. Функция возвращает только те
 значения, которым во втором списке идет True (с тем же индексом)'''

from itertools import compress

data = 'ABCDEF'
selectors = [True, False, True, False, True, False]
new_data = list(compress(data, selectors))
#print(new_data)

# Функция выполняется до тех пор, пока в одной из переданных
# последовательностей не закончатся элементы

selectors = [True, False, True]
new_data = list(compress(data, selectors))
#print(new_data)

# Функция compress() эквивалентна следующему коду:

def compress(iterable, selectors):
    for it, sel in zip(iterable, selectors):
        if sel:
            yield it

''' Функция islice(iterable, start, stop, step) 
 возвращает итератор, элементы которого укладываются в указанный
 диапазон значений. По сути, это срез.
 старт - по умолчанию 0
 стоп - берется не включительно. Должен быть передан обязательно,
 если последовательность нужна до конца, то ставится None
 степ - по умолчанию равен 1
 Функция не поддерживает отрицательные значения для аргументов'''

from itertools import islice

#print(*islice(range(10), None))
#print(*islice(range(100), 5))
#print(*islice(range(100), 5, 10))
#print(*islice(range(200), 0, None, 20))

''' Функция chain() последовательно генерирует
 элементы всех переданных ему последовательностей'''

from itertools import chain

chain_iter1 = chain('ABC', 'DEF')
chain_iter2 = chain(enumerate('ABC'))
chain_iter3 = chain('abc', [1, 2, 3, 4], ('8', '0'),
                    {'one': 1, 'two': 2})

#print(*chain_iter1)
#print(*chain_iter2)
#print(*chain_iter3)
#print()

def chain(*iterables):
    for iter in iterables:
        for elem in iter:
            yield elem

''' Функция chain.from_iterable() принимает итерируемый объекс,
 содержащий в качестве элементов другие итерируемые объекты. 
 Возвращает итератор, который генерирует элементы
 всех вложенных итерируемых объектов'''
from itertools import chain

chain_iter1 = list(chain.from_iterable(['ABC', 'DEF']))
chain_iter1 = chain.from_iterable(['ABC', 'DEF'])
chain_iter2 = chain.from_iterable(enumerate('ABC'))
chain_iter3 = chain.from_iterable(['abc', [1, 2, 3, 4], ('8', '0'),
                    {'one': 1, 'two': 2}])
#print(*chain_iter1)
#print(*chain_iter2)
#print(*chain_iter3)
#print()

def chain_from_iterable(iterable):
    for it in iterable:
        for elem in it:
            yield elem

''' Функция zip_longest(*iterables, fillvalue=None) возвращает
 итератор, объединяющий элементы переданных последовательностей
 в кортежи. В отличие от zip() останавливается при достижении
 последнего элемента у самой длинной последовательности.
 Недостающие элементы заменяются на fillvalue'''

from itertools import zip_longest

#print(*zip([1, 2, 3], ['a', 'b', 'c', 'd', 'e']))
#print(*zip_longest([1, 2, 3], ['a', 'b', 'c', 'd', 'e']))
#print(*zip_longest([1, 2, 3], ['a', 'b', 'c', 'd', 'e'], fillvalue='*'))
#print(*zip_longest(['a', 'b', 'c', 'd', 'e'], [1, 2, 3], fillvalue=777))

''' Функция tee(iterable, n) возвращает кортеж, содержащий 
 n независимых итераторов на основе переданной 
 последовательности. n по умолчанию равен 2'''

from itertools import tee

iter1, iter2 = tee([1, 'a', 2, 'b', 3, 'c'])
#print(*iter1)
#print(*iter2)

result = tee(range(2, 5), 4)
#print(type(result))
#for i in result:
#    print(*i)

# Новые созданные итераторы будут меняться, если изменить
# исходную последовательность

from itertools import tee

data = [1, 2, 3, 4, 5]
iter1, iter2 = tee(data)
data.append(6)
#print(*iter1)
#print(*iter2)

''' Функция pairwise(iterable) возвращает итератор,
 содержащий последовательно перекрывающиеся пары
 в виде кортежей, взятые из исходной последовательности'''

#from itertools import pairwise

#print(*pairwise('ABCDEFG'))
#print(*pairwise([1, 2, 3, 4, 5]))


#('A', 'B') ('B', 'C') ('C', 'D') ('D', 'E') ('E', 'F') ('F', 'G')
#(1, 2) (2, 3) (3, 4) (4, 5)
#Функция pairwise() примерно эквивалентна следующему коду:

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

# Добавлена только в Питоне 3.10

''' Функция groupby() используетя для группировки
 смежных элементов итерируемого объекта. Она 
 возвращает итератор, содержащий кортежи, каждый из которых
 состоит из 2х элементов: первый - значение, которое 
 является общим для всех элементов группы; второе - 
 итератор, содержащий непосредственно элементы группы'''

from itertools import groupby

numbers = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]
group_iter = groupby(numbers)
#print(type(group_iter))
#print(*group_iter, sep='\n')

# Ого! второй элемент вывода - сама группа - тоже итератор!
# Чтобы её посмотреть, используем обычные для итератора методы:
# распаковка, пробежаться циклом, преобразование

#for key, value in group_iter:
    #print(f'{key}: {list(value)}')
#print()
# Отсортируем список, чтобы все элементы разбились по группам,
# и не было повторяющихся групп

group_iter = groupby(sorted(numbers))
#for k, v in group_iter:
    #print(f'{k}: {list(v)}')
#print()

''' Функция groupby() имеет необязательный аргумент
 key , который определяет правило группировки. Она
 имеет тот же смысл, как в функциях min, max, sort'''

group_iter = groupby(numbers, key=lambda num: num < 10)
#for k, v in group_iter:
    #print(f'{k}: {list(v)}')
#print()

# Делаем предварительную сортировку по тому же key

key_func = lambda num: num < 10
group_iter = groupby(sorted(numbers, key=key_func), key=key_func)
#for k, v in group_iter:
    #print(f'{k}: {list(v)}')

# Нужно сортировать по той же функции, что используется и в groupby

# Посчитаем самый часто встречающиющийся символ
data = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'D', 'A', 'A', 'B', 'B', 'B']
group_iter = groupby(sorted(data))
max_result = max(group_iter, key=lambda tpl: sum(1 for i in tpl[1]))
#print(max_result[0])

# Когда последовательно обращаешься к последовательностям
# groupby, он стирает те элементы, которые уже прошел, потому что это итераторы
group_iter = groupby(numbers)
group1 = next(group_iter)[1]
#print(list(group1))

group2 = next(group_iter)[1]
#print(list(group1))
#print(list(group2))

''' Функци permutatinos(iterable, r=None) возвращает итератор,
 который содержит все перестановки из элементов 
 переданного итерируемого объекта. Каждая перестановка 
 заключена в кортеж нужно длины - аргумент r. По умлочнаию 
 r равен None, значит кортежи будут той же дины, что и 
 переданная последовательность '''

from itertools import permutations

numbers = [1, 2, 3, 4]
letters = 'def'

nums = permutations(numbers)
lets = permutations(letters)

#print(list(nums))
#print(list(lets))

# передаем аргументы

nums = [1, 2, 3, 4]
#print(list(permutations(nums, 1)))
#print(list(permutations(nums, 2)))
#print(list(permutations(nums, 3)))
#print()

''' Данная функция создает размещение н по к: произвольный упорядоченный
 набор, состоящий из к различных элементов данного
 множества '''

''' Функция combinations(iterable, r)  имеет такой же
синтаксис, но создает неупорядоченный набор - сочетание н по к.
'''

from itertools import combinations
letters = [1, 2, 3, 4]
#print(list(combinations(letters, 1)))
#print(list(combinations(letters, 2)))
#print(list(combinations(letters, 3)))
#print(list(combinations(letters, 4)))
#print()

''' Функция combination_with_replacement(iterable, r) 
 возвращает итератор, который содержит все слчетания
 элементов итерируемого объекта с повторами'''

from itertools import combinations_with_replacement as c_w_r

nums = [1, 2, 3, 4]

#print(list(c_w_r(nums, 1)))
#print(list(c_w_r(nums, 2)))
#print(list(c_w_r(nums, 3)))

''' Разница: 
combinations - это все значения, 
но без одинаковых значений и без отзеркаливания:
(1, 2) (1, 3) (2, 3)

permutations - все значения, 
но с отзеркаливанием:
(1, 2) (1, 3) (2, 1) (2, 3) (3, 1) (3, 2)

combinations_with_replacement - 
с одинаковыми значениями, но без отзеркаливания
(1, 1) (1, 2) (1, 3) (2, 2) (2, 3) (3, 3)'''

''' Функция product(*iterables, repeat) возвращает итератор, который 
 содержит декартово произведение всех переданных 
 итерируемых объектов. Декартово произведение - 
 это как результат АВС и XYZ-анализа (матрица 
  из всех возможных вариантов сочетаний'''

from itertools import product

numbers = [1, 2]
letters = ['x', 'y', 'z']
flags = [False, True]

#print(list(product(numbers, letters)))
#print(list(product(letters, numbers)))
#print(list(product(letters, numbers, flags)))

# Порядок передачи последовательностей имеет значение!

''' repeat нужен для вычисления декартова произведения
 с самим собой'''

letters = 'abc'
#print(list(product(letters, repeat=2)))

'''  repeat можно использовать и когда последовательностей
несколько, интересный результат :)'''

letters = ['x', 'z']
#print(list(product(numbers, letters, repeat=2)))

'''  Функцию product() удобно использовать для замены вложенных циклов'''
import time
start_time = time.perf_counter()
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(f'{hours} : {minutes} : {seconds}')
end_time = time.perf_counter()
work_time = end_time - start_time


# этот цикл заменяет следующий код:
start_time2 = time.perf_counter()
for t in product(range(24), range(60), range(60)):
    print(*t, sep=' : ')
end_time2 = time.perf_counter()
work_time2 = end_time2 - start_time2
print(f'Время работы программы = {work_time}')
print(f'Время работы программы = {work_time2}')

# Но работает он дольше, чем циклы


