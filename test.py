import numpy as np
import sort
import search


def main():
    length = 10
    seq = np.random.randint(0, 100, (length))
    print(seq)
    # sort.insertion(seq[::], length)
    # print(seq)
    sort.selection(seq[::], length)
    print(seq)
    # search.linear(seq, length)


if __name__ == '__main__':
    main()