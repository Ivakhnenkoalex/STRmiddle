def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return (a)


def ft_find_second_char(char, str):
    d = ft_len(str)
    k = 0
    i = 0
    b = char
    while d > i:
        if str[i] == b:
            k = k + 1
        i = i + 1
    if k == 1:
        return -1
    if k >= 2:
        i = 0
        k = 0
        while d > i:
            if str[i] == b:
                k = k + 1
                if k == 1:
                    n = i
                if k == 2:
                    m = i

            i = i + 1
        return n, m
    else:
        return -2
