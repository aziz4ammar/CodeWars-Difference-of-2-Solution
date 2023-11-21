def twos_difference(lst):
    m = sorted(lst)
    t = []
    for i in range(len(m)):
        if m[i] + 2 in m:
            t.append((m[i], m[i] + 2))
    return t