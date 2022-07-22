def get_permutations(w):
    if len(w) <= 1:
        return set(w)

    smaller = get_permutations(w[1:])
    parms = set()

    for x in smaller:
        for pos in range(0, len(x) + 1):
            parm = x[:pos] + w[0] + x[pos:]
            parms.add(parm)

    return parms


result = get_permutations('Washingtom')

print(result, len(result))
