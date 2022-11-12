from random import randint


def get_unique_list_numbers() -> list[int]:
    i = 1
    list_ = [randint(-10, 10)]
    while i < 15:
        a = randint(-10, 10)
        if list_.count(a) == 0:
            list_.insert(i, a)
            i += 1
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
