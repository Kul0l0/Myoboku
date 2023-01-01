def linear(seq, x):
    res = None
    for idx, value in enumerate(seq):
        if value == x:
            return idx
        elif value > x:
            break
        else:
            continue
    return res
