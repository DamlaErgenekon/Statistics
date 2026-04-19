import random
def weighted_srs(data, n, weights, with_replacement=False):
    if with_replacement: return random.choices(data, weights=weights, k=n)
    d, w, s = list(data), list(weights), []
    for i in range(n):
        idx = d.index(random.choices(d, weights=w, k=1)[0])
        s.append(d.pop(idx))
        w.pop(idx)
    return s
