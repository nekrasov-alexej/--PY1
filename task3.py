def delete(list_, index=None):
    if index != None:
        list1 = slice(0, index)
        list2 = slice(index + 1, len(list_))
        list_1 = list_[list1]
        list_2 = list_[list2]
        list_r = list_1 + list_2
    else:
        listr = slice(0, len(list_) - 1)
        list_r = list_[listr]
    return list_r
print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
