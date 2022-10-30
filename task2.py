import string


def get_count_char(str_):
    str_l = str_.lower()
    str_split = str_l.split()
    str_j = ''.join(str_split)
    str_r = ''
    for i in range(len(str_j)-1):
        if str_j[i].isalpha() == 1:
            str_r = str_r + str_j[i]
    dict_ = {str_r[i]: str_r.count(str_r[i]) for i in range(len(str_r)-1)}
    return dict_
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
