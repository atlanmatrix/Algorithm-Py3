def merge(a: list, b: list) -> list:
    ai = bi = 0
    res_lst = []
    while ai < len(a) and bi < len(b):
        if a[ai] <= b[bi]:
            res_lst.append(a[ai])
            ai += 1
        else:
            res_lst.append(b[bi])
            bi += 1
    if ai == len(a):
        for i in b[bi:]:
            res_lst.append(i)
    else:
        for i in a[ai:]:
            res_lst.append(i)

    return res_lst


if __name__ == "__main__":
    print(merge([-1], [2,2,4]))
