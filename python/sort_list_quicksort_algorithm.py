def qsort(l):
    if l == []:
        return []
    return qsort([x for x in l[1:] if x < l[0]]) + l[0:1] + qsort([x for x in l[1:] if x >= l[0]])


lst = [44, 33, 22, 5, 77, 55, 999, 1]

print(qsort(lst))
