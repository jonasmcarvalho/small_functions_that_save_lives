from cgitb import reset
import enum


def find_pairs(l, x):
    pairs = []
    for(i, el_1) in enumerate(l):
        for(j, el_2) in enumerate(l[i+1:]):
            if el_1 + el_2 == x:
                pairs.append((el_1, el_2))

    return pairs


list = [1, 5, 3, 9, 6, 7, 2, 4, 8]

# result = find_pairs(list, 3)

print('1 = ', find_pairs(list, 1))
print('2 = ', find_pairs(list, 2))
print('3 = ', find_pairs(list, 3))
print('4 = ', find_pairs(list, 4))
print('5 = ', find_pairs(list, 5))
print('6 = ', find_pairs(list, 6))
print('7 = ', find_pairs(list, 7))
print('8 = ', find_pairs(list, 8))
print('9 = ', find_pairs(list, 9))
