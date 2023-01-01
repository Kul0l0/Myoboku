def insertion(seq, length, increasing=True):
    # increasing or decreasing
    ic_coeff = 1 if increasing is True else -1
    for newcard_idx in range(1, length):
        newcard = seq[newcard_idx]
        idx = newcard_idx-1
        # find the insertion position
        while idx >= 0 and ic_coeff*newcard < ic_coeff*seq[idx]:
            seq[idx+1] = seq[idx]
            idx -= 1
        seq[idx+1] = newcard


def selection(seq, length):
    for left_length in range(length)[:0:-1]:
        # find max value index
        max_value_idx = 0
        for idx in range(left_length+1)[1:]:
            if seq[idx] > seq[max_value_idx]:
                max_value_idx = idx
        seq[left_length], seq[max_value_idx] = seq[max_value_idx], seq[left_length]
        print(seq, max_value_idx)