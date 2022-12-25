def insertion(seq, length):
    for newcard_idx in range(1, length):
        newcard = seq[newcard_idx]
        idx = newcard_idx-1
        # find the insertion position
        while idx >= 0 and newcard < seq[idx]:
            seq[idx+1] = seq[idx]
            idx -= 1
        seq[idx+1] = newcard
