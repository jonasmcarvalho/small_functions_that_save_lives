def intersect(lst1, lst2):
    res, lst2_copy = [], lst2[:]
    for el in lst1:
        if el in lst2_copy:
            res.append(el)
            lst2_copy.remove(el)
    return res


list1 = [1, 2, 3, 5]
list2 = [3, 7, 2, 4]

print(intersect(list1, list2))
