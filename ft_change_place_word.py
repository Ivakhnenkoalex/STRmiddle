def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return (a)


def ft_change_place_word(str):
    d = ft_len(str)
    s = ''
    i = 0
    k = 0
    z = d
    while d > i:
        if str[i] == ' ':
            k = i + 1
        i = i + 1
    d = z
    i = 0
    s = str[k:d] + ' ' + str[i:k]
    return s
