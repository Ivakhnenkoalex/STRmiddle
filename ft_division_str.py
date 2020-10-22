def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return (a)


def ft_division_str(str):
    d = ft_len(str)
    s = ''
    i = 0
    z = d
    if d % 2 == 0:
        d = d // 2
        s = str[d:z] + str[i:d]
        return s
    else:
        d = d // 2 + 1
        s = str[d:z] + str[i:d]
        return s



