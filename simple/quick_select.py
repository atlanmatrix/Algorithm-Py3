import random


def quick_select(lst, no, low, high):
    pi = partition(lst, low, high)

    if low < high:
        if pi < no - 1:
            quick_select(lst, no, pi + 1, high)
        elif pi > no - 1:
            quick_select(lst, no, low, pi - 1)
        else:
            print(f'Lucky Get: ', pi + 1, lst[pi])
    else:
        print(f'Get: ', no, lst[no - 1])


def partition(lst, low, high):
    pi = low
    pi_val = lst[pi]
    print('->  ', [_ if low <= idx <= high else "" for idx, _ in enumerate(lst)], '  <===>  ', lst)

    lst[pi], lst[high] = lst[high], lst[pi]

    for i in range(low, high):
        if lst[i] > pi_val:
            lst[pi], lst[i] = lst[i], lst[pi]
            pi += 1
    lst[pi], lst[high] = lst[high], lst[pi]
    print('<-  ', [_ if low <= idx <= high else "" for idx, _ in enumerate(lst)], '  <===>  ', lst)

    return pi


if __name__ == "__main__":
    n = 20
    lst = [random.randrange(10, 100) for _ in range(n)]

    no = random.randint(1, n)
    print(f'Get {no} from {lst}')
    print('=' * 100)
    l = 0
    r = len(lst) - 1
    quick_select(lst, no, l, r)
