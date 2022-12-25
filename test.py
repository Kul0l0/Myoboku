import numpy as np
import sort


def main():
    seq = np.random.randint(0, 100, (20))
    print(seq)
    sort.insertion(seq, 20)
    print(seq)


if __name__ == '__main__':
    main()